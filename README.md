# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_20:16:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,372 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 20:16:07 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.009 |  |
| 2026-06-24 20:13:54 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.018 |  |
| 2026-06-24 20:12:36 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:11:28 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.076 |  |
| 2026-06-24 20:10:24 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-24 20:08:52 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:07:44 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:07:27 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:06:01 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-06-24 20:06:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:05:53 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.042 |  |
| 2026-06-24 20:05:45 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:04:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:04:51 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:04:06 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-06-24 20:03:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-06-24 20:03:44 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:03:37 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-06-24 20:03:34 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:03:27 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.247 |  |
| 2026-06-24 20:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.031 |  |
| 2026-06-24 20:03:12 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-24 20:03:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:02:43 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.119 |  |
| 2026-06-24 20:02:42 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:02:19 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:02:12 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.050 |  |
| 2026-06-24 20:02:10 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:02:01 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-06-24 20:01:54 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:01:52 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:01:40 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:01:34 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.085 |  |
| 2026-06-24 20:00:43 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:00:27 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.100 |  |
| 2026-06-24 19:51:31 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 20:02:01 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-06-24 20:10:24 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-24 20:03:12 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-24 20:00:43 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:02:19 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:03:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:03:34 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:07:27 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:02:10 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:01:54 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:04:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:07:44 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:01:52 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:06:00 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:08:52 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:12:36 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:05:45 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:01:40 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 20:16:07 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.009 |  |
| 2026-06-24 20:06:01 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-06-24 20:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:03:44 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:02:42 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:04:51 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-24 20:13:54 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.018 |  |
| 2026-06-24 20:04:06 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-06-24 20:03:37 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-06-24 20:03:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-06-24 20:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.031 |  |
| 2026-06-24 20:05:53 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.042 |  |
| 2026-06-24 20:02:12 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.050 |  |
| 2026-06-24 20:11:28 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.076 |  |
| 2026-06-24 20:01:34 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.085 |  |
| 2026-06-24 20:00:27 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.100 |  |
| 2026-06-24 20:02:43 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.119 |  |
| 2026-06-24 20:03:27 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)