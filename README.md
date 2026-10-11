# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_19:18:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 19:18:15 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:15:33 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-11 19:15:33 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 19:11:53 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-11 19:10:14 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-10-11 19:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.027 |  |
| 2026-10-11 19:07:32 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-10-11 19:06:44 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.079 |  |
| 2026-10-11 19:06:29 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-10-11 19:06:29 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-11 19:06:17 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-11 19:05:52 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.039 |  |
| 2026-10-11 19:05:28 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-11 19:05:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 19:04:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-11 19:04:07 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-10-11 19:03:52 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-11 19:03:22 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-11 19:03:22 | Moragaswewa (Deduru Oya) | 2.07 | 🟢 Normal | -0.087 |  |
| 2026-10-11 19:03:10 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 19:03:07 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 19:03:03 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 19:02:52 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-10-11 19:02:44 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 19:02:37 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.051 |  |
| 2026-10-11 19:02:30 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.030 |  |
| 2026-10-11 19:02:18 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:02:08 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-11 19:01:56 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-11 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 19:01:17 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-11 19:01:14 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 19:00:58 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-11 19:00:46 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:00:39 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 19:06:29 | Ellagawa (Kalu Ganga) | 6.88 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-10-11 19:02:52 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-10-11 19:04:07 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-10-11 19:03:52 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-11 19:06:17 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-11 19:05:28 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-11 19:01:56 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-11 19:03:22 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-11 19:11:53 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-11 19:00:39 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-11 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 19:15:33 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 19:03:07 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 19:05:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 19:01:12 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 19:03:10 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 19:03:03 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 19:02:44 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 19:15:33 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-11 19:02:18 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:00:46 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:01:14 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:18:15 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 19:10:14 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-11 19:02:08 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-11 19:00:58 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-11 19:06:29 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-11 19:01:17 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-11 19:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.027 |  |
| 2026-10-11 19:07:32 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-10-11 19:02:30 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.030 |  |
| 2026-10-11 19:04:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-11 19:05:52 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.039 |  |
| 2026-10-11 19:02:37 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.051 |  |
| 2026-10-11 19:06:44 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.079 |  |
| 2026-10-11 19:03:22 | Moragaswewa (Deduru Oya) | 2.07 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)