# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_16:45:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 16:45:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:28:21 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-25 16:15:37 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-25 16:14:05 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.041 |  |
| 2026-05-25 16:12:06 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-05-25 16:07:52 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:51 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-25 16:07:48 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-05-25 16:07:43 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 16:07:35 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:13 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:00 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:06:15 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.028 |  |
| 2026-05-25 16:05:49 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-25 16:05:35 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:48 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:48 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-25 16:04:39 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:27 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.098 |  |
| 2026-05-25 16:04:25 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-05-25 16:04:08 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:07 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-05-25 16:04:01 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:03:57 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.091 |  |
| 2026-05-25 16:02:51 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:02:44 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-05-25 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.041 |  |
| 2026-05-25 16:02:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-25 16:02:05 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-05-25 16:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:40 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:34 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:23 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | -0.071 |  |
| 2026-05-25 16:01:21 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 16:01:13 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:09 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-25 16:00:42 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:00:35 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-05-25 15:59:40 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.041 |  |
| 2026-05-25 16:15:37 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-25 16:28:21 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-25 16:05:49 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-25 15:59:40 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-25 16:01:21 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 16:07:51 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-25 16:07:43 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 16:01:34 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:00 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:00:42 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:40 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:08 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:35 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:01:13 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:45:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:01 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:04:48 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:52 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:07:13 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:05:35 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:02:51 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 16:12:06 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-05-25 16:01:09 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-25 16:02:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-25 16:00:35 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-05-25 16:04:07 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-05-25 16:04:48 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-25 16:06:15 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.028 |  |
| 2026-05-25 16:04:25 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-05-25 16:02:44 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-05-25 16:14:05 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.041 |  |
| 2026-05-25 16:07:48 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-05-25 16:02:05 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-05-25 16:01:23 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | -0.071 |  |
| 2026-05-25 16:03:57 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.091 |  |
| 2026-05-25 16:04:27 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)