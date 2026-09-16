# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_00:08:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 00:08:01 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.131 |  |
| 2026-09-17 00:07:41 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.037 |  |
| 2026-09-17 00:07:13 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-17 00:06:34 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 00:06:33 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-17 00:06:29 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:05:31 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:05:12 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:04:53 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-17 00:04:52 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-17 00:04:50 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 00:04:46 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:04:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:04:04 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:04:01 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.020 |  |
| 2026-09-17 00:03:52 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 00:03:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:03:40 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:03:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:54 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:52 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 00:02:50 | Magura (Kalu Ganga) | 3.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 00:02:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:46 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-09-17 00:02:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:25 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-09-17 00:02:24 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-17 00:02:22 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 00:02:22 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:01:49 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 00:01:44 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:01:39 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:01:33 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.073 |  |
| 2026-09-17 00:01:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-17 00:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-09-17 00:00:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 23:46:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-16 23:42:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 00:04:53 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-17 00:02:24 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-17 00:01:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-17 00:07:13 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-17 00:06:33 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-17 00:06:34 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 00:02:50 | Magura (Kalu Ganga) | 3.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 00:01:49 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 00:04:50 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 00:03:52 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 00:02:22 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 00:02:52 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 23:46:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:04:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:03:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:03:40 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:54 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:00:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:22 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:05:31 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:06:29 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:02:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 00:03:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:04:46 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:01:44 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-17 00:04:04 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:07:58 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.012 |  |
| 2026-09-17 00:02:46 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-09-17 00:04:01 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.020 |  |
| 2026-09-16 23:02:12 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-09-17 00:02:25 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-09-17 00:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-09-17 00:07:41 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.037 |  |
| 2026-09-17 00:01:33 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.073 |  |
| 2026-09-17 00:08:01 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)