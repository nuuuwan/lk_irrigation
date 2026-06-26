# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_03:11:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,399 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 03:11:06 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-27 03:10:50 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:10:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:08:52 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-27 03:08:41 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.003 |  |
| 2026-06-27 03:08:05 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:07:14 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:06:25 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-06-27 03:05:58 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2026-06-27 03:05:57 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:05:51 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:05:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.086 |  |
| 2026-06-27 03:04:57 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 03:04:48 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:40 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:34 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:16 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.028 |  |
| 2026-06-27 03:04:12 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:02 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.132 |  |
| 2026-06-27 03:03:58 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.048 |  |
| 2026-06-27 03:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:03:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:31 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:30 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:23 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-27 03:02:14 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-27 03:01:43 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 03:01:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:24 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 03:01:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:13 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-06-27 03:01:00 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:22:07 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 03:11:06 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-27 03:08:52 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-27 03:01:24 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 03:01:43 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 03:04:57 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 03:08:41 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.003 |  |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:31 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:02:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:03:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:40 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:34 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:44:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:08:05 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:07:14 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:04:48 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:05:51 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 02:08:05 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:10:50 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:10:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-27 03:01:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:05:57 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-27 02:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-27 03:01:13 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-06-27 03:05:58 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2026-06-27 03:02:14 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-27 03:02:23 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-27 02:03:02 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-06-27 03:06:25 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-06-27 03:04:16 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.028 |  |
| 2026-06-27 03:03:58 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.048 |  |
| 2026-06-27 03:05:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.086 |  |
| 2026-06-27 03:04:02 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)