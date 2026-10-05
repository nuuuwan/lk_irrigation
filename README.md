# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_10:27:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,479 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 10:27:20 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:21:59 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:12:50 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:12:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-10-05 10:10:13 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:09:37 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-10-05 10:09:27 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.046 |  |
| 2026-10-05 10:08:43 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.036 |  |
| 2026-10-05 10:08:40 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:08:15 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-10-05 10:08:09 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.039 |  |
| 2026-10-05 10:07:27 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-10-05 10:07:09 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.077 |  |
| 2026-10-05 10:05:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:05:27 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 10:05:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 10:05:19 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.097 |  |
| 2026-10-05 10:05:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:04:48 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-05 10:04:37 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-05 10:04:24 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 10:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.030 |  |
| 2026-10-05 10:03:44 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.010 |  |
| 2026-10-05 10:03:26 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.324 |  |
| 2026-10-05 10:03:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-05 10:02:38 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.269 |  |
| 2026-10-05 10:02:33 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 10:02:27 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-10-05 10:02:23 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.050 |  |
| 2026-10-05 10:02:21 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 10:02:12 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.112 |  |
| 2026-10-05 10:01:49 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:31 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:23 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.032 |  |
| 2026-10-05 10:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-05 10:01:16 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:12 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.056 |  |
| 2026-10-05 10:01:12 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-05 10:00:51 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 10:01:12 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-05 10:05:27 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 10:04:48 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-05 10:05:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 10:02:33 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 10:04:24 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 10:04:37 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-05 10:02:21 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 10:01:16 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:31 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:05:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:21:59 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:08:40 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:00:51 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:05:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:01:49 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:12:50 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:27:20 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 10:12:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-10-05 10:08:15 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-10-05 10:03:44 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.010 |  |
| 2026-10-05 10:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-05 10:03:13 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-05 10:09:37 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-10-05 10:07:27 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-10-05 10:02:27 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-10-05 10:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.030 |  |
| 2026-10-05 10:01:23 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.032 |  |
| 2026-10-05 10:08:43 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.036 |  |
| 2026-10-05 10:08:09 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.039 |  |
| 2026-10-05 10:09:27 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.046 |  |
| 2026-10-05 10:02:23 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.050 |  |
| 2026-10-05 10:01:12 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.056 |  |
| 2026-10-05 10:07:09 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.077 |  |
| 2026-10-05 10:05:19 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.097 |  |
| 2026-10-05 10:02:12 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.112 |  |
| 2026-10-05 10:02:38 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.269 |  |
| 2026-10-05 10:03:26 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.324 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)