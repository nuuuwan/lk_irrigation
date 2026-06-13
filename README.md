# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_17:13:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 17:13:13 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:10:51 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:09:38 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.010 |  |
| 2026-06-13 17:09:03 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.019 |  |
| 2026-06-13 17:09:02 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.040 |  |
| 2026-06-13 17:08:31 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.066 |  |
| 2026-06-13 17:07:38 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:07:26 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.019 |  |
| 2026-06-13 17:07:20 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-13 17:07:10 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | -0.011 |  |
| 2026-06-13 17:06:30 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.051 |  |
| 2026-06-13 17:06:15 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.066 |  |
| 2026-06-13 17:05:43 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 17:05:42 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | -0.090 |  |
| 2026-06-13 17:05:40 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.089 |  |
| 2026-06-13 17:05:17 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2026-06-13 17:05:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-13 17:04:34 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.011 |  |
| 2026-06-13 17:04:21 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:03:53 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-13 17:03:08 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.005 |  |
| 2026-06-13 17:02:51 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 17:02:50 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:02:40 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:02:39 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -89.182 |  |
| 2026-06-13 17:02:37 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:02:31 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 17:02:22 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.52 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-06-13 17:01:44 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 17:01:44 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:01:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:01:18 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-06-13 17:00:59 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-13 17:00:30 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:00:27 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | -89.182 |  |
| 2026-06-13 17:00:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.123 |  |
| 2026-06-13 17:00:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.52 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-06-13 17:07:10 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | -0.011 |  |
| 2026-06-13 17:07:20 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-13 17:01:44 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 17:02:22 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 17:05:43 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 17:02:31 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 17:02:51 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 17:03:08 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.005 |  |
| 2026-06-13 17:01:44 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:00:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:01:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:10:51 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:00:30 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:02:37 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:07:38 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:03:53 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:02:40 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 16:02:44 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:04:21 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:13:13 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:02:50 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 17:09:38 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.010 |  |
| 2026-06-13 17:05:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-13 17:00:59 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-13 17:04:34 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.011 |  |
| 2026-06-13 17:01:18 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-06-13 17:07:26 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.019 |  |
| 2026-06-13 17:09:03 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.019 |  |
| 2026-06-13 17:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-13 17:09:02 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.040 |  |
| 2026-06-13 17:06:30 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.051 |  |
| 2026-06-13 17:06:15 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.066 |  |
| 2026-06-13 17:08:31 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | -0.066 |  |
| 2026-06-13 17:05:17 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2026-06-13 17:05:40 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.089 |  |
| 2026-06-13 17:05:42 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | -0.090 |  |
| 2026-06-13 17:00:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.123 |  |
| 2026-06-13 17:02:39 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -89.182 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)