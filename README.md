# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_06:31:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 06:31:37 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | -0.002 |  |
| 2026-09-13 06:14:09 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-09-13 06:10:43 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:09:16 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.423 | 🔺 Rising |
| 2026-09-13 06:09:13 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:07:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.229 |  |
| 2026-09-13 06:07:34 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-13 06:07:16 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 06:06:50 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 06:06:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:06:20 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 06:05:57 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 06:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-13 06:05:03 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.039 |  |
| 2026-09-13 06:04:32 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:04:19 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-13 06:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 2.551 | 🔺 Rising |
| 2026-09-13 06:03:49 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-13 06:03:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:03:26 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-09-13 06:03:09 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.088 |  |
| 2026-09-13 06:03:03 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-09-13 06:03:02 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:02:59 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:02:41 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.067 |  |
| 2026-09-13 06:02:41 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-13 06:02:29 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | 0.311 | 🔺 Rising |
| 2026-09-13 06:02:22 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:02:09 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 06:02:00 | Weraganthota (Mahaweli Ganga) | -3.63 | 🟢 Normal | -0.005 |  |
| 2026-09-13 06:01:41 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-13 06:01:24 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:01:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:01:05 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:00:59 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:00:56 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 06:00:52 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:00:23 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:57:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 2.551 | 🔺 Rising |
| 2026-09-13 05:57:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 2.551 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 06:02:29 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | 0.311 | 🔺 Rising |
| 2026-09-13 06:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 2.551 | 🔺 Rising |
| 2026-09-13 06:09:16 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.423 | 🔺 Rising |
| 2026-09-13 06:03:26 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-09-13 06:03:03 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-09-13 06:07:34 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-13 06:04:19 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-13 06:01:41 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-13 06:03:49 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-13 06:05:57 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 06:02:09 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 06:00:56 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 06:07:16 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 06:06:50 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 06:02:41 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-13 06:06:20 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 06:00:23 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:03:02 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:09:13 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:01:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:02:59 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:01:05 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:10:43 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:03:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:00:59 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:04:32 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:06:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:00:52 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:45 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:01:24 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:02:22 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 06:31:37 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | -0.002 |  |
| 2026-09-13 06:02:00 | Weraganthota (Mahaweli Ganga) | -3.63 | 🟢 Normal | -0.005 |  |
| 2026-09-13 06:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-13 06:14:09 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-09-13 06:05:03 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.039 |  |
| 2026-09-13 06:02:41 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.067 |  |
| 2026-09-13 06:03:09 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.088 |  |
| 2026-09-13 06:07:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)