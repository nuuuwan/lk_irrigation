# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_21:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,564 measurements** from **39** stations.
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
| 2026-08-14 21:18:24 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:12:38 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:12:08 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:11:11 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:10:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:10:16 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.018 |  |
| 2026-08-14 21:10:15 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-14 21:08:22 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:07:00 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.057 |  |
| 2026-08-14 21:06:34 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.058 |  |
| 2026-08-14 21:06:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:06:09 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:05:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:05:22 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 21:05:18 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-14 21:04:58 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-14 21:04:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:04:20 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:03:39 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.147 |  |
| 2026-08-14 21:03:24 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.032 |  |
| 2026-08-14 21:03:03 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.042 |  |
| 2026-08-14 21:02:51 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:42 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-14 21:02:32 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-14 21:02:19 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:15 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:14 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-08-14 21:02:12 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:01:48 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-14 21:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:01:45 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-08-14 21:01:08 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-14 21:00:59 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-14 21:00:52 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:00:13 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 21:05:18 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-14 21:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-14 21:02:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-14 21:01:08 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-14 21:00:59 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-14 21:05:22 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 21:10:15 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-14 21:00:13 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:04:20 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:08:22 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:51 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:19 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:02:32 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:12:38 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:18:24 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:10:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:04:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:00:52 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:42 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:05:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:15 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:12:08 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:06:09 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:06:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:32 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:04:58 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-14 21:01:48 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-14 21:01:45 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-08-14 21:10:16 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.018 |  |
| 2026-08-14 21:02:14 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-08-14 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-08-14 21:03:24 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.032 |  |
| 2026-08-14 21:03:03 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.042 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-14 21:07:00 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.057 |  |
| 2026-08-14 21:06:34 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.058 |  |
| 2026-08-14 21:03:39 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)