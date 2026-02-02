# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_09:07:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,309 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 09:07:21 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-02 09:06:41 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:06:34 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:06:22 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:57 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:35 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.040 |  |
| 2026-02-02 09:05:33 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:27 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:24 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:56 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:32 | Thanthirimale (Malwathu Oya) | 2.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 09:04:21 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:16 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:04:15 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:11 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:48 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:47 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:45 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:03:34 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:31 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.147 |  |
| 2026-02-02 09:02:34 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:02:20 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-02 09:02:13 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-02-02 09:02:05 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:01:58 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:01:26 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-02-02 09:01:19 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-02 09:01:18 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.043 |  |
| 2026-02-02 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:01:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:00:45 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-02 09:00:39 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:00:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.165 |  |
| 2026-02-02 08:38:46 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.165 |  |
| 2026-02-02 08:33:18 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:14:04 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:14:02 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-02-02 08:12:27 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 09:01:26 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-02-02 09:00:45 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-02 09:02:20 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-02 09:01:19 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-02 09:07:21 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-02 09:04:32 | Thanthirimale (Malwathu Oya) | 2.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 08:00:54 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 09:01:58 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:02:13 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:00:39 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:48 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:47 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:56 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:06:22 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:33 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:02:05 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:01:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:15 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:06:34 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:57 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:24 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-02-02 08:02:02 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:05:27 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:04:21 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:34 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 09:03:45 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:04:16 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:06:41 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:04:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-02 09:02:34 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-02 08:12:27 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.012 |  |
| 2026-02-02 09:05:35 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.040 |  |
| 2026-02-02 08:14:02 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.042 |  |
| 2026-02-02 09:01:18 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.043 |  |
| 2026-02-02 07:03:50 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.055 |  |
| 2026-02-02 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-02-02 09:03:31 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.147 |  |
| 2026-02-02 09:00:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)