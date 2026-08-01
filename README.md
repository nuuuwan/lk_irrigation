# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_09:20:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,930 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 09:20:23 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-01 09:17:50 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:09:52 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-08-01 09:09:04 | Peradeniya (Mahaweli Ganga) | 5.85 | 🟡 Alert | 0.420 | 🔺 Rising |
| 2026-08-01 09:09:02 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.026 |  |
| 2026-08-01 09:07:39 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-08-01 09:07:31 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.073 |  |
| 2026-08-01 09:07:05 | Glencourse (Kelani Ganga) | 14.45 | 🟢 Normal | 0.565 | 🔺 Rising |
| 2026-08-01 09:06:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:06:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-08-01 09:06:10 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-01 09:06:06 | Holombuwa (Kelani Ganga) | 2.79 | 🟢 Normal | -0.550 |  |
| 2026-08-01 09:05:50 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:04:59 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:04:36 | Deraniyagala (Kelani Ganga) | 3.29 | 🟢 Normal | -1.001 |  |
| 2026-08-01 09:04:31 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.055 |  |
| 2026-08-01 09:04:29 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-01 09:04:05 | Kithulgala (Kelani Ganga) | 2.60 | 🟢 Normal | -0.402 |  |
| 2026-08-01 09:04:04 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-01 09:03:52 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.793 | 🔺 Rising |
| 2026-08-01 09:03:49 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:46 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:38 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:20 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-08-01 09:03:13 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:57 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:53 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:33 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-08-01 09:02:15 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-08-01 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-08-01 09:02:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:08 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:06 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:01:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2026-08-01 09:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:01:15 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-08-01 09:01:00 | Nawalapitiya (Mahaweli Ganga) | 3.65 | 🟡 Alert | -0.502 |  |
| 2026-08-01 09:00:54 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:00:49 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-01 08:35:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 09:09:04 | Peradeniya (Mahaweli Ganga) | 5.85 | 🟡 Alert | 0.420 | 🔺 Rising |
| 2026-08-01 09:01:00 | Nawalapitiya (Mahaweli Ganga) | 3.65 | 🟡 Alert | -0.502 |  |
| 2026-08-01 09:03:52 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.793 | 🔺 Rising |
| 2026-08-01 09:07:05 | Glencourse (Kelani Ganga) | 14.45 | 🟢 Normal | 0.565 | 🔺 Rising |
| 2026-08-01 09:09:52 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-08-01 09:07:39 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-08-01 09:06:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-08-01 09:20:23 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-01 09:02:33 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-08-01 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-08-01 09:04:29 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-01 09:06:10 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-01 08:26:48 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-01 09:02:53 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:06 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:04:59 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:00:54 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:13 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:57 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:17:50 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:06:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:46 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:38 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:02:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:00:49 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:03:49 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:05:50 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 09:04:04 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-01 09:02:15 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-08-01 09:03:20 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-08-01 09:09:02 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.026 |  |
| 2026-08-01 09:04:31 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.055 |  |
| 2026-08-01 09:01:15 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-08-01 09:01:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2026-08-01 09:07:31 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.073 |  |
| 2026-08-01 09:04:05 | Kithulgala (Kelani Ganga) | 2.60 | 🟢 Normal | -0.402 |  |
| 2026-08-01 09:06:06 | Holombuwa (Kelani Ganga) | 2.79 | 🟢 Normal | -0.550 |  |
| 2026-08-01 09:04:36 | Deraniyagala (Kelani Ganga) | 3.29 | 🟢 Normal | -1.001 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)