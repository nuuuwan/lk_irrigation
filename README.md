# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_12:09:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,591 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 12:09:59 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-05-31 12:09:57 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2026-05-31 12:09:11 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.009 |  |
| 2026-05-31 12:08:39 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:08:06 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:07:20 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:06:46 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:06:37 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-05-31 12:05:46 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:05:05 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-05-31 12:04:29 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-05-31 12:04:19 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-05-31 12:03:59 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:46 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-05-31 12:03:29 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:29 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:05 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | -0.043 |  |
| 2026-05-31 12:03:00 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-31 12:02:59 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:50 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:49 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-31 12:02:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-31 12:02:35 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:31 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:28 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.041 |  |
| 2026-05-31 12:02:27 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-05-31 12:02:25 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:23 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:21 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.052 |  |
| 2026-05-31 12:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-05-31 12:02:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:00 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.022 |  |
| 2026-05-31 12:01:48 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:43 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:39 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:38 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.029 |  |
| 2026-05-31 12:00:45 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 11:42:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 11:31:50 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 11:28:28 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 12:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.041 |  |
| 2026-05-31 12:02:49 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-31 12:02:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-31 12:02:28 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:43 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 11:16:22 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:50 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:29 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:08:39 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:29 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:07:20 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:03:59 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:25 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:59 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:39 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:08:06 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:35 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:00:45 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:02:23 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:05:46 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:01:48 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:06:46 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 12:09:57 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.009 |  |
| 2026-05-31 12:09:11 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.009 |  |
| 2026-05-31 12:03:00 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-31 12:06:37 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-05-31 12:05:05 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-05-31 12:03:46 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-05-31 12:02:00 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.022 |  |
| 2026-05-31 12:09:59 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-05-31 12:01:38 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.029 |  |
| 2026-05-31 12:04:29 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-05-31 12:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-05-31 12:02:27 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-05-31 12:04:19 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-05-31 12:03:05 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | -0.043 |  |
| 2026-05-31 12:02:21 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)