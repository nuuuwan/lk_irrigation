# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_13:00:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,996 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 13:00:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:13:58 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 12:03:37 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-06-06 12:03:23 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-06 12:04:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-06 12:07:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 12:03:28 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 12:01:20 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:02:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:22 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:02:16 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:00:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:05:18 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:03:21 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:29 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:04:23 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:05:00 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:05:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:05:29 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:42 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:24 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:53 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:02:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:06:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-06-06 12:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-06 12:02:54 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-06 12:01:58 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-06-06 12:01:34 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-06 12:04:23 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-06-06 12:04:23 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.031 |  |
| 2026-06-06 12:08:02 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.031 |  |
| 2026-06-06 12:05:46 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.031 |  |
| 2026-06-06 12:02:10 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-06-06 12:06:09 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.040 |  |
| 2026-06-06 12:03:56 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.049 |  |
| 2026-06-06 12:03:09 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.051 |  |
| 2026-06-06 12:02:23 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.052 |  |
| 2026-06-06 12:04:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)