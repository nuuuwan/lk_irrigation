# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_03:16:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,094 measurements** from **39** stations.
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
| 2026-08-12 03:16:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.011 |  |
| 2026-08-12 03:13:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-08-12 03:10:13 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:09:55 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.036 |  |
| 2026-08-12 03:08:12 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 03:07:16 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 03:07:04 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:07:03 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:06:36 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:06:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.005 |  |
| 2026-08-12 03:06:11 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-08-12 03:06:08 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:05:53 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:05:31 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:05:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:05:23 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -54.000 |  |
| 2026-08-12 03:05:21 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -54.000 |  |
| 2026-08-12 03:05:19 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-12 03:05:18 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-12 03:04:51 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:04:39 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-12 03:04:17 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-12 03:04:16 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-08-12 03:04:11 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:04:06 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:34 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:34 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:28 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-08-12 03:03:26 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:19 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-08-12 03:03:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.005 |  |
| 2026-08-12 03:03:05 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:04 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:04 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:02:45 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:02:40 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:02:09 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-08-12 03:01:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:36 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.020 |  |
| 2026-08-12 03:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 03:05:19 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-12 00:01:58 | Weraganthota (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-08-12 03:13:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-08-12 03:07:16 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 03:08:12 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 03:05:31 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:05:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:26 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:07:04 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:04 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:05:53 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:04:51 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:06:36 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:34 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:02:40 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:04 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:06:08 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:10:13 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:04:11 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:04:06 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:05 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:03:34 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:06:20 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.005 |  |
| 2026-08-12 03:03:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.005 |  |
| 2026-08-12 03:06:11 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-08-12 03:04:39 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-12 03:04:16 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-08-12 03:03:19 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-08-12 03:16:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.011 |  |
| 2026-08-12 03:03:28 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-08-12 03:01:36 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.020 |  |
| 2026-08-12 03:02:09 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-08-12 03:09:55 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.036 |  |
| 2026-08-12 03:05:23 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)