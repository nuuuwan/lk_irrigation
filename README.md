# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_05:34:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 05:34:57 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-16 05:27:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:11:22 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.084 |  |
| 2026-09-16 05:10:13 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 05:09:53 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.186 |  |
| 2026-09-16 05:09:49 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.099 |  |
| 2026-09-16 05:09:46 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.051 |  |
| 2026-09-16 05:09:32 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:08:39 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.076 |  |
| 2026-09-16 05:07:52 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.031 |  |
| 2026-09-16 05:07:03 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -216.000 |  |
| 2026-09-16 05:07:02 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -216.000 |  |
| 2026-09-16 05:06:39 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:06:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:06:38 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:05:44 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-16 05:05:04 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:04:43 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-16 05:04:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-16 05:04:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:04:05 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-16 05:03:34 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-09-16 05:03:02 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-09-16 05:02:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:02:44 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.069 |  |
| 2026-09-16 05:02:31 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.080 |  |
| 2026-09-16 05:02:30 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.252 |  |
| 2026-09-16 05:02:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:01:53 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:01:42 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.049 |  |
| 2026-09-16 05:01:40 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:01:32 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:01:13 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-09-16 05:01:11 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -2.182 |  |
| 2026-09-16 05:00:38 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -2.182 |  |
| 2026-09-16 05:00:34 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 05:04:43 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-16 05:04:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-16 05:05:44 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-16 05:10:13 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 05:34:57 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-16 05:01:32 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:01:53 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:02:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:00:34 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:27:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:06:39 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:05:04 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:02:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:04:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:06:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:09:32 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-16 05:01:40 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-16 05:04:05 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-16 05:03:02 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-09-16 05:03:34 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-09-16 05:01:13 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-09-16 05:07:52 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.031 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-16 05:01:42 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.049 |  |
| 2026-09-16 05:09:46 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.051 |  |
| 2026-09-16 05:02:44 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.069 |  |
| 2026-09-16 05:08:39 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.076 |  |
| 2026-09-16 05:02:31 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.080 |  |
| 2026-09-16 05:11:22 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.084 |  |
| 2026-09-16 05:09:49 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.099 |  |
| 2026-09-16 04:08:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.139 |  |
| 2026-09-16 05:09:53 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.186 |  |
| 2026-09-16 05:02:30 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.252 |  |
| 2026-09-16 04:49:11 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -1.609 |  |
| 2026-09-16 05:01:11 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -2.182 |  |
| 2026-09-16 05:07:03 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)