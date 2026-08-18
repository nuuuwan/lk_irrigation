# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_11:24:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,743 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 11:24:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:17:55 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:12:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.044 |  |
| 2026-08-18 11:11:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-08-18 11:10:05 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:09:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:09:16 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-18 11:09:05 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:07:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-18 11:07:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-18 11:06:34 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.047 |  |
| 2026-08-18 11:06:30 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.032 |  |
| 2026-08-18 11:05:22 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:05:22 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 11:07:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-18 11:07:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-18 11:04:55 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-18 11:02:46 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 11:03:24 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 11:00:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:09:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:02:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:05:02 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:01:23 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:10:05 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:04:15 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:02:06 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:02:30 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:04:37 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:09:05 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:00:52 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:03:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:17:55 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:01:37 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:04:16 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:24:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:03:37 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:05:22 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-18 11:11:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-08-18 11:09:16 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-18 11:01:47 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-18 11:01:33 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-18 10:02:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-18 11:04:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.022 |  |
| 2026-08-18 11:02:36 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.030 |  |
| 2026-08-18 11:03:34 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.030 |  |
| 2026-08-18 11:06:30 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.032 |  |
| 2026-08-18 11:03:28 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.041 |  |
| 2026-08-18 11:00:15 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.042 |  |
| 2026-08-18 11:02:00 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.042 |  |
| 2026-08-18 11:12:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.044 |  |
| 2026-08-18 11:06:34 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.047 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)