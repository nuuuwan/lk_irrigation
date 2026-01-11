# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_10:46:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,591 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 10:46:01 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:18:36 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:12:09 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-01-11 10:09:12 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 10:08:30 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:07:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:06:48 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-01-11 10:05:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-11 10:05:33 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-01-11 10:04:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:04:46 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:04:36 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-11 10:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.062 |  |
| 2026-01-11 10:03:49 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:03:40 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-11 10:03:28 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:03:23 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 10:03:21 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:03:05 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.166 |  |
| 2026-01-11 10:02:53 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:02:38 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:36 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-01-11 10:02:30 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:29 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 10:02:27 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:24 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:17 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:14 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.065 |  |
| 2026-01-11 10:02:07 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:55 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:43 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:31 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 10:01:20 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:11 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:08 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-01-11 10:00:57 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:00:11 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 10:04:36 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-11 10:03:40 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-11 10:01:31 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 10:03:23 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 10:02:29 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 10:09:12 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 10:01:55 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:11 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:00:11 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:20 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:07 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:18:36 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:38 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:03:28 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:24 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:27 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:04:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:00:57 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:08:30 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:04:46 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:17 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:46:01 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:01:43 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:30 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:12:09 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-01-11 10:05:33 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-01-11 10:06:48 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-01-11 10:03:49 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:07:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:02:53 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:03:21 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-11 10:02:36 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-01-11 10:05:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-11 10:01:08 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-01-11 10:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.062 |  |
| 2026-01-11 10:02:14 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.065 |  |
| 2026-01-11 10:03:05 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)