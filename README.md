# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_17:08:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,751 measurements** from **39** stations.
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
| 2026-10-05 17:08:03 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.631 | 🔺 Rising |
| 2026-10-05 17:07:47 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:07:39 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-05 17:07:36 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-05 17:06:47 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:06:44 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-05 17:05:30 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.082 |  |
| 2026-10-05 17:05:27 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.033 |  |
| 2026-10-05 17:05:14 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-10-05 17:05:10 | Nawalapitiya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-10-05 17:04:48 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:04:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-05 17:04:24 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-10-05 17:04:21 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-10-05 17:04:19 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.059 |  |
| 2026-10-05 17:04:16 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-10-05 17:04:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-10-05 17:04:02 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:03:58 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:03:45 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.091 |  |
| 2026-10-05 17:03:35 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 17:03:18 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:03:04 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-05 17:03:02 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.059 |  |
| 2026-10-05 17:02:53 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.081 |  |
| 2026-10-05 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.060 |  |
| 2026-10-05 17:02:17 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.060 |  |
| 2026-10-05 17:01:44 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 17:01:28 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:01:09 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:01:06 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:01:00 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:00:41 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2026-10-05 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-10-05 17:00:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:00:08 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:26:53 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | -0.023 |  |
| 2026-10-05 16:26:31 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 17:08:03 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.631 | 🔺 Rising |
| 2026-10-05 17:05:14 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-10-05 17:07:36 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-05 17:05:10 | Nawalapitiya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-10-05 17:07:39 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-05 17:06:44 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-05 17:03:35 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 17:01:44 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 17:01:00 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:01:09 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:03:18 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:04:48 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:06:47 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:00:08 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:03:58 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:07:47 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:01:28 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:01:06 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:04:02 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:11:31 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-05 17:00:08 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:26:31 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.008 |  |
| 2026-10-05 17:03:04 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-05 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-10-05 17:00:41 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2026-10-05 17:04:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-05 17:04:24 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-10-05 16:26:53 | Panadugama (Nilwala Ganga) | 3.48 | 🟢 Normal | -0.023 |  |
| 2026-10-05 17:05:27 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.033 |  |
| 2026-10-05 17:04:21 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-10-05 17:04:16 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-10-05 17:04:19 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.059 |  |
| 2026-10-05 17:03:02 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.059 |  |
| 2026-10-05 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.060 |  |
| 2026-10-05 17:02:17 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.060 |  |
| 2026-10-05 17:04:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-10-05 17:02:53 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.081 |  |
| 2026-10-05 17:05:30 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.082 |  |
| 2026-10-05 17:03:45 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)