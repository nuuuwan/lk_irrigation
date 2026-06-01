# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_06:31:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 06:31:32 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.001 |  |
| 2026-06-01 06:21:09 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-06-01 06:10:16 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:08:02 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 06:07:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.112 |  |
| 2026-06-01 06:05:53 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:05:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 06:03:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-01 06:01:12 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-01 06:00:26 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-01 06:08:02 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 06:05:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:04:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:01:28 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:03:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:01:57 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:00:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:03:33 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:04:49 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:05:53 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:03:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:05:13 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:04:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:02:16 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:10:16 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:02:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:01:18 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 06:31:32 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.001 |  |
| 2026-06-01 06:04:34 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-06-01 06:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-06-01 06:02:17 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-01 06:21:09 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-06-01 05:02:21 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-01 06:02:24 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-01 06:00:41 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-06-01 06:00:56 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.013 |  |
| 2026-06-01 06:03:43 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-01 06:01:05 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-06-01 06:03:33 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.020 |  |
| 2026-06-01 06:01:59 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-01 06:01:52 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.022 |  |
| 2026-06-01 06:05:08 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.038 |  |
| 2026-06-01 06:01:39 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.070 |  |
| 2026-06-01 06:07:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.112 |  |
| 2026-06-01 06:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)