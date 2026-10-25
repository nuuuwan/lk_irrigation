# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_06:29:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,307 measurements** from **39** stations.
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
| 2026-10-25 06:29:00 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.039 |  |
| 2026-10-25 06:20:12 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:18:14 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 06:15:17 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-25 06:12:46 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-25 06:11:04 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:10:06 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-25 06:09:48 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-25 06:09:22 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:09:22 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.050 |  |
| 2026-10-25 06:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-10-25 06:06:59 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 06:06:50 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:06:12 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.153 |  |
| 2026-10-25 06:05:23 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.224 |  |
| 2026-10-25 06:05:16 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.793 |  |
| 2026-10-25 06:05:08 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:04:46 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-10-25 06:04:39 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:04:36 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.021 |  |
| 2026-10-25 06:04:30 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-25 06:04:03 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-25 06:03:54 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.103 |  |
| 2026-10-25 06:03:41 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-25 06:03:35 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-25 06:03:34 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:03:19 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-25 06:03:15 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.005 |  |
| 2026-10-25 06:03:09 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 06:02:18 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:02:16 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:02:02 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 06:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:01:23 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-25 06:01:18 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:01:14 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-10-25 06:00:55 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 06:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-10-25 06:09:48 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-25 06:04:03 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-25 06:03:19 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-25 06:10:06 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-25 06:04:30 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-25 06:03:41 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-25 06:02:02 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 06:01:23 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-25 06:12:46 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-25 06:06:59 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 06:03:09 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 06:18:14 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 06:11:04 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:05:08 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:04:39 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:09:22 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:20:12 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:01:18 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:02:16 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-25 06:03:15 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.005 |  |
| 2026-10-25 06:15:17 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-25 06:02:18 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:06:50 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:03:34 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:00:55 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-25 06:04:46 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-10-25 06:03:35 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-25 06:04:36 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.021 |  |
| 2026-10-25 06:01:14 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-25 06:29:00 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.039 |  |
| 2026-10-25 06:09:22 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.050 |  |
| 2026-10-25 06:03:54 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.103 |  |
| 2026-10-25 06:06:12 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.153 |  |
| 2026-10-25 06:05:23 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.224 |  |
| 2026-10-25 06:05:16 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.793 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)