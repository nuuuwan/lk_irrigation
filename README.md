# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_23:08:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,868 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 23:08:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 23:06:14 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 23:05:00 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 23:04:59 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.021 |  |
| 2026-10-06 23:04:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:04:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 23:04:14 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-06 23:04:09 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-10-06 23:03:54 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 23:03:49 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-06 23:03:44 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.586 | 🔺 Rising |
| 2026-10-06 23:03:42 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:03:42 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-10-06 23:03:39 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 23:03:32 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-06 23:03:22 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-06 23:03:20 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-06 23:03:18 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2026-10-06 23:03:02 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-06 23:02:27 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.119 |  |
| 2026-10-06 23:02:07 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.020 |  |
| 2026-10-06 23:01:58 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:43 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.043 |  |
| 2026-10-06 23:01:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:23 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-10-06 23:01:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 23:01:07 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:00:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:00:35 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 23:03:44 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.586 | 🔺 Rising |
| 2026-10-06 23:01:23 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-10-06 23:03:22 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-06 23:03:32 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-06 23:06:14 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 23:08:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-06 23:05:00 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 23:03:20 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-06 23:03:02 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-06 22:10:47 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-06 23:04:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 23:03:39 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 23:03:54 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 23:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 23:01:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 23:01:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:58 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:00:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:07 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-06 22:00:36 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:01:43 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:00:35 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:04:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:03:42 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-06 23:04:09 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-10-06 23:03:42 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-10-06 23:04:14 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-06 23:03:49 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-06 23:02:07 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.020 |  |
| 2026-10-06 23:04:59 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.021 |  |
| 2026-10-06 22:34:00 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-10-06 23:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.043 |  |
| 2026-10-06 23:03:18 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2026-10-06 23:02:27 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.119 |  |
| 2026-10-06 22:03:27 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)