# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_04:04:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,181 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 04:04:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-05 04:03:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:03:18 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:03:11 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:38 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:02:04 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:03 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-05-05 04:01:40 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-05-05 04:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:00:53 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.042 |  |
| 2026-05-05 04:00:25 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.074 |  |
| 2026-05-05 03:11:45 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 03:05:10 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-05 01:20:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-05 01:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-05 04:04:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-04 23:06:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-05 03:08:55 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-05 03:06:47 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.002 |  |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:01:51 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:04 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:01:51 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 02:59:30 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:03:58 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:10:22 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:04:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:06:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:03:11 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:03:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:38 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:08:27 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:09:18 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.002 |  |
| 2026-05-05 03:04:16 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-05 04:02:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:03:18 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-05-05 02:11:59 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-05-05 04:01:40 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-05-05 03:04:09 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.032 |  |
| 2026-05-05 04:00:53 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.042 |  |
| 2026-05-05 03:11:45 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-05-05 03:05:50 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.061 |  |
| 2026-05-05 04:00:25 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.074 |  |
| 2026-05-05 04:02:03 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-05-05 03:07:09 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.160 |  |
| 2026-05-05 03:03:33 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)