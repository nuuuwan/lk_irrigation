# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_13:02:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,841 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 13:02:36 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-08-27 13:02:33 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:02:32 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.030 |  |
| 2026-08-27 13:02:13 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:02:05 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 13:01:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-08-27 13:01:42 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:01:29 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-27 13:01:11 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-08-27 13:01:04 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.053 |  |
| 2026-08-27 13:01:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:00:51 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:00:32 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:00:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:21:12 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 13:01:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-08-27 12:00:46 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-27 13:02:05 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 12:06:25 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 12:06:30 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 13:02:33 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:00:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:01:36 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:02:13 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:04:30 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:03:11 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:07:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:21:12 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:01:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:00:32 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:02:32 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:01:42 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:03:55 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 13:00:51 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:00:50 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:02:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:06:23 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-27 12:04:44 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-08-27 12:03:50 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-27 13:01:11 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-08-27 13:02:36 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-08-27 12:02:41 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.011 |  |
| 2026-08-27 12:01:32 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-08-27 12:13:15 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.017 |  |
| 2026-08-27 12:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-08-27 13:01:29 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-27 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.030 |  |
| 2026-08-27 12:02:26 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-08-27 12:05:19 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.049 |  |
| 2026-08-27 12:03:34 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.049 |  |
| 2026-08-27 13:01:04 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.053 |  |
| 2026-08-27 12:03:24 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.055 |  |
| 2026-08-27 12:02:53 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)