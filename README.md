# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_02:10:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,137 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 02:10:19 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:09:30 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:07:42 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.005 |  |
| 2026-06-29 02:07:26 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-29 02:06:17 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 02:06:08 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:05:57 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 02:05:55 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:05:54 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-29 02:04:57 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.005 |  |
| 2026-06-29 02:04:07 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:03:48 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 02:03:39 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:03:20 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:23 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-29 02:02:05 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:05 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:01:48 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.180 |  |
| 2026-06-29 02:01:27 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:01:23 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 02:01:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-29 02:01:11 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 01:37:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-29 01:33:17 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-29 01:24:36 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 01:03:35 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-29 01:13:23 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-29 01:37:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-29 02:01:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-29 02:07:26 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-29 00:10:01 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 02:05:57 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 02:01:23 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 01:05:53 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 02:03:48 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 02:06:17 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 01:06:56 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:00:35 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:10:19 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:01:27 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:05 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:04:07 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-29 01:00:51 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:03:39 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 01:03:37 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:06:08 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:03:20 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:05:55 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:09:30 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:01:11 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:02:23 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:08:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 02:04:57 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.005 |  |
| 2026-06-29 02:07:42 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.005 |  |
| 2026-06-29 02:05:54 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 02:02:16 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-29 01:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.041 |  |
| 2026-06-29 02:01:48 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)