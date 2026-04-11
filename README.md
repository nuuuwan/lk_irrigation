# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_09:07:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 09:07:06 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:06:30 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-11 09:05:28 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-04-11 09:04:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:04:29 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:04:09 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-04-11 09:04:04 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-04-11 09:03:54 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-04-11 09:03:32 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:03:18 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:03:14 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:03:10 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.147 |  |
| 2026-04-11 09:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:02:57 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:55 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-04-11 09:02:47 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:02:30 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:19 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-04-11 09:02:10 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:03 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:01:43 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-11 09:01:30 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-11 09:01:22 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 09:01:14 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:01:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:01:06 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:00:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:00:39 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:58:24 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.005 |  |
| 2026-04-11 08:54:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:16:30 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:16:24 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.084 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 09:03:54 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-04-11 09:01:43 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-11 09:01:30 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-11 09:06:30 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-11 08:09:55 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-11 09:01:22 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 09:02:55 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:01:14 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:08:24 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:04:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:03:32 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:57 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:03:18 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:30 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:07:06 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:03 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:00:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:47 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:25 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:04:29 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:00:39 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:10 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:48 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-11 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:58:24 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.005 |  |
| 2026-04-11 08:10:14 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-04-11 09:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-11 08:07:35 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:01:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:02:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-11 09:03:14 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-11 08:01:58 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-04-11 09:05:28 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-04-11 08:05:52 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-11 09:04:09 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-04-11 09:04:04 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-04-11 09:02:19 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-04-11 09:02:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-04-11 09:03:10 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)