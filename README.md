# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_17:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,578 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 17:12:38 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-18 17:11:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:10:24 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:08:43 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:08:22 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:08:03 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:07:54 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-02-18 17:07:53 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:07:47 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:07:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.228 |  |
| 2026-02-18 17:06:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:06:05 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:06:05 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.049 |  |
| 2026-02-18 17:05:46 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:05:22 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:05:21 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.015 |  |
| 2026-02-18 17:05:14 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:04:30 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-18 17:04:25 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:04:05 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 17:04:02 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:03:32 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:03:08 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-18 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:48 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:46 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.060 |  |
| 2026-02-18 17:02:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-18 17:02:24 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:20 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 17:04:30 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-18 17:01:24 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-18 17:12:38 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-18 17:01:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 17:04:05 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 17:02:48 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:01:56 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:00:24 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:08:22 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:08:43 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:01:38 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:07:53 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:10:24 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:07:47 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:00:44 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:05:22 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:24 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:11:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:03:32 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:04:02 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:20 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 16:03:40 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:05:46 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:06:05 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:05:14 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:04 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:06:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:04:25 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:08:03 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-18 17:01:46 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-02-18 17:02:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-18 17:03:08 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-18 17:05:21 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.015 |  |
| 2026-02-18 17:07:54 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-02-18 17:01:38 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.020 |  |
| 2026-02-18 17:06:05 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.049 |  |
| 2026-02-18 17:02:46 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.060 |  |
| 2026-02-18 17:07:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)