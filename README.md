# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_09:14:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Norwood — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 09:14:52 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.026 |  |
| 2026-10-26 09:13:58 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.036 |  |
| 2026-10-26 09:10:42 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-10-26 09:09:55 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 09:09:29 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-10-26 09:08:43 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.081 |  |
| 2026-10-26 09:08:33 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-26 09:08:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:07:44 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 09:07:27 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.038 |  |
| 2026-10-26 09:07:17 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:06:58 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-26 09:06:46 | Moragaswewa (Deduru Oya) | 4.10 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-26 09:06:26 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-26 09:06:23 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.029 |  |
| 2026-10-26 09:06:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-26 09:05:55 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 09:04:57 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:04:57 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | 0.335 | 🔺 Rising |
| 2026-10-26 09:04:40 | Norwood (Kelani Ganga) | 1.65 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-10-26 09:04:13 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:04:02 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.021 |  |
| 2026-10-26 09:03:51 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 09:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.65 | 🟡 Alert | 0.200 | 🔺 Rising |
| 2026-10-26 09:03:36 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.073 |  |
| 2026-10-26 09:03:33 | Galgamuwa (Mee Oya) | 2.61 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-26 09:03:26 | Giriulla (Maha Oya) | 3.02 | 🟢 Normal | -0.021 |  |
| 2026-10-26 09:02:48 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 09:02:22 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.660 | 🔺 Rising |
| 2026-10-26 09:02:21 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-10-26 09:02:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 09:02:15 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-26 09:01:55 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-10-26 09:01:44 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-26 09:01:18 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-10-26 09:01:12 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:00:34 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:00:32 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.046 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 09:04:57 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | 0.335 | 🔺 Rising |
| 2026-10-26 09:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.65 | 🟡 Alert | 0.200 | 🔺 Rising |
| 2026-10-26 09:04:40 | Norwood (Kelani Ganga) | 1.65 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-10-26 09:06:23 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.029 |  |
| 2026-10-26 09:02:22 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.660 | 🔺 Rising |
| 2026-10-26 09:10:42 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-10-26 09:02:21 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-10-26 09:03:33 | Galgamuwa (Mee Oya) | 2.61 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-26 09:06:26 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-26 08:02:03 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-26 09:06:46 | Moragaswewa (Deduru Oya) | 4.10 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-26 09:02:15 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-26 09:08:33 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-26 09:06:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-26 09:01:44 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-26 09:00:32 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-26 09:03:51 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 09:02:48 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 09:06:58 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-26 09:07:44 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 09:05:55 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 09:09:55 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 09:02:19 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 09:04:13 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:01:12 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:04:57 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:07:17 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:00:34 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:08:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 09:01:18 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-10-26 09:09:29 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-10-26 09:04:02 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.021 |  |
| 2026-10-26 09:01:55 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-10-26 09:03:26 | Giriulla (Maha Oya) | 3.02 | 🟢 Normal | -0.021 |  |
| 2026-10-26 09:14:52 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.026 |  |
| 2026-10-26 09:13:58 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.036 |  |
| 2026-10-26 09:07:27 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.038 |  |
| 2026-10-26 09:03:36 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.073 |  |
| 2026-10-26 09:08:43 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)