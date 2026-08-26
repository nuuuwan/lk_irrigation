# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_01:05:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,403 measurements** from **39** stations.
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
| 2026-08-27 01:05:12 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-08-27 01:05:06 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:03:56 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 01:03:52 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:03:14 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-27 01:02:53 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.021 |  |
| 2026-08-27 01:02:35 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-27 01:02:07 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-08-27 01:02:05 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 01:02:02 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:01:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-27 01:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:00:48 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 01:00:25 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:19:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 00:02:25 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-08-27 01:05:12 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-08-27 00:11:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-27 00:05:22 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-27 00:03:02 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-27 01:03:14 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-27 00:10:23 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-27 01:02:35 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-27 01:00:48 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 01:02:05 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-27 01:03:56 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 00:13:06 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-27 01:05:06 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:00:27 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:02:02 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:03:52 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:06:32 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:09 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:05:59 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:00:25 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:01:53 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:06:08 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:04:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:08:00 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:07:23 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-27 01:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:03:34 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-27 00:07:53 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-08-27 01:01:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:01:52 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-27 00:06:47 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-08-27 00:13:24 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.014 |  |
| 2026-08-26 18:01:25 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-08-27 00:02:08 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-08-27 01:02:53 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.021 |  |
| 2026-08-27 00:19:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.021 |  |
| 2026-08-27 01:02:07 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)