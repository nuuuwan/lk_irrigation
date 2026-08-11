# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_16:18:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,693 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 16:18:06 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:16:36 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-08-11 16:14:50 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:13:57 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.017 |  |
| 2026-08-11 16:13:53 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:11:49 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:09:45 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:08:58 | Peradeniya (Mahaweli Ganga) | 3.39 | 🟢 Normal | -0.009 |  |
| 2026-08-11 16:08:34 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-08-11 16:07:54 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.028 |  |
| 2026-08-11 16:07:37 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:06:20 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:04:44 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:04:34 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:04:06 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:03:43 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:03:42 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-08-11 16:03:33 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:03:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:03:13 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:02:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:02:54 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -6.367 |  |
| 2026-08-11 16:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:02:49 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-11 16:02:41 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.020 |  |
| 2026-08-11 16:02:39 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 16:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:02:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-08-11 16:02:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:02:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.069 |  |
| 2026-08-11 16:02:18 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:02:11 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:42 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 16:01:25 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:22 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:14 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:06 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:00 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:00:48 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 15:58:00 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -6.367 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 16:08:34 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-08-11 16:02:49 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-11 16:02:39 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 16:01:42 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 16:01:06 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:18:06 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:25 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:02:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:22 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:14 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:09:45 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:13:53 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:04:34 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:03:43 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:11:49 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:03:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:02:11 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:14:50 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:01:00 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-08-11 16:08:58 | Peradeniya (Mahaweli Ganga) | 3.39 | 🟢 Normal | -0.009 |  |
| 2026-08-11 16:06:20 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:04:44 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:03:33 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:07:37 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:04:06 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:02:18 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:03:13 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-11 16:16:36 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-08-11 16:13:57 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.017 |  |
| 2026-08-11 16:02:41 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.020 |  |
| 2026-08-11 16:07:54 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.028 |  |
| 2026-08-11 16:03:42 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-08-11 15:08:08 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-08-11 16:02:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-08-11 16:02:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.069 |  |
| 2026-08-11 16:02:54 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -6.367 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)