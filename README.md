# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_12:31:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 12:31:16 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-25 12:11:14 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 12:08:49 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:07:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-25 12:06:24 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 12:04:59 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-08-25 12:04:56 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:04:54 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.677 |  |
| 2026-08-25 12:04:44 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-08-25 12:04:43 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-08-25 12:04:29 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:04:27 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-08-25 12:04:25 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:56 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-25 12:03:46 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-08-25 12:03:42 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:34 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-25 12:03:12 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-25 12:03:11 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:03 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-25 12:02:52 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:37 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 12:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-25 12:02:19 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:09 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-08-25 12:02:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-25 12:02:01 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-08-25 12:02:01 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:00 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-25 12:01:14 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.049 |  |
| 2026-08-25 12:01:10 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-08-25 12:00:52 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:00:26 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 12:04:44 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-08-25 12:03:03 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-25 12:07:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-25 12:03:56 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-25 12:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-25 12:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-25 12:02:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-25 12:03:34 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-25 12:06:24 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 12:02:37 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 12:31:16 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-25 12:03:12 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-25 12:11:14 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 12:02:01 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:00:52 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:04:25 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:04:29 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:52 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:04:56 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:00 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 11:04:07 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:11 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:03:42 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:08:49 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:00:26 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:19 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:02:09 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-08-25 12:00:17 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-25 12:04:59 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-08-25 12:04:43 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-08-25 12:03:46 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-08-25 12:01:10 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-08-25 12:02:01 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-08-25 12:04:27 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-08-25 12:01:14 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.049 |  |
| 2026-08-25 12:04:54 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.677 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)