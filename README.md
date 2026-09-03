# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_09:13:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,578 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 09:13:22 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.085 |  |
| 2026-09-03 09:08:51 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:43 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:35 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:04 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:07:34 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.043 |  |
| 2026-09-03 09:07:18 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:06:59 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:06:49 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:06:27 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:05:45 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.135 |  |
| 2026-09-03 09:05:15 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:05:06 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.106 |  |
| 2026-09-03 09:05:01 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:04:43 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:04:38 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.011 |  |
| 2026-09-03 09:03:49 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:03:30 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:25 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-09-03 09:03:24 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:20 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:14 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:03:12 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-09-03 09:02:34 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:02:34 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:02:32 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 09:02:28 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:02:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:46 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:30 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:16 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.063 |  |
| 2026-09-03 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-09-03 09:01:09 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:08 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.045 |  |
| 2026-09-03 09:00:38 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:00:21 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 6.415 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 09:00:21 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 6.415 | 🔺 Rising |
| 2026-09-03 09:02:32 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 09:02:34 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:09 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:24 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:02:34 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:00:38 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:05:15 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:30 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:35 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:43 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:03:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:07:18 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:06:27 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:05:01 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:51 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:04:43 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:02:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:06:59 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:06:49 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:30 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 08:20:01 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:01:46 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 09:08:04 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:03:49 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:02:28 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:03:14 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-09-03 09:03:12 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-09-03 09:04:38 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.011 |  |
| 2026-09-03 09:07:34 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.043 |  |
| 2026-09-03 09:01:08 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.045 |  |
| 2026-09-03 09:03:25 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-09-03 09:01:16 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.063 |  |
| 2026-09-03 09:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-09-03 09:13:22 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.085 |  |
| 2026-09-03 09:05:06 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.106 |  |
| 2026-09-03 09:05:45 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)