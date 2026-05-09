# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_14:24:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,141 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 14:24:57 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:19:59 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-05-09 14:19:19 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:16:12 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:13:13 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.058 |  |
| 2026-05-09 14:12:54 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:10:28 | Moragaswewa (Deduru Oya) | 3.32 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-09 14:09:28 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-05-09 14:09:27 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.046 |  |
| 2026-05-09 14:09:11 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-05-09 14:09:06 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:07:49 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-05-09 14:07:12 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:06:09 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-09 14:05:54 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-09 14:05:54 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.019 |  |
| 2026-05-09 14:05:31 | Thanamalwila (Kirindi Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:05:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-05-09 14:05:08 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.028 |  |
| 2026-05-09 14:04:41 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.042 |  |
| 2026-05-09 14:04:30 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-09 14:04:26 | Katharagama (Menik Ganga) | 2.22 | 🟢 Normal | -0.080 |  |
| 2026-05-09 14:04:22 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-05-09 14:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.056 |  |
| 2026-05-09 14:03:44 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.059 |  |
| 2026-05-09 14:03:35 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:03:34 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-05-09 14:03:19 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.158 |  |
| 2026-05-09 14:03:17 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-09 14:02:59 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.050 |  |
| 2026-05-09 14:02:14 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.014 |  |
| 2026-05-09 14:01:57 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:01:30 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 156.522 | 🔺 Rising |
| 2026-05-09 14:01:27 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.043 |  |
| 2026-05-09 14:01:11 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:01:07 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 156.522 | 🔺 Rising |
| 2026-05-09 14:00:33 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-05-09 14:00:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 13:55:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.378 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 14:01:30 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 156.522 | 🔺 Rising |
| 2026-05-09 14:05:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-05-09 14:06:09 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-09 14:10:28 | Moragaswewa (Deduru Oya) | 3.32 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-09 14:04:30 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-09 14:09:06 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:19:19 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:03:35 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 12:59:46 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:00:28 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:01:57 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:12:54 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:24:57 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:09:28 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-05-09 14:05:31 | Thanamalwila (Kirindi Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:03:17 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:07:12 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:01:11 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | -0.010 |  |
| 2026-05-09 14:09:11 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-05-09 14:00:33 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-05-09 14:02:14 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.014 |  |
| 2026-05-09 14:07:49 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-05-09 14:05:54 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.019 |  |
| 2026-05-09 14:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-09 14:05:08 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.028 |  |
| 2026-05-09 14:05:54 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-09 14:04:22 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-05-09 14:19:59 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-05-09 14:04:41 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.042 |  |
| 2026-05-09 14:01:27 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.043 |  |
| 2026-05-09 14:09:27 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.046 |  |
| 2026-05-09 14:02:59 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.050 |  |
| 2026-05-09 14:03:34 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-05-09 14:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.056 |  |
| 2026-05-09 14:13:13 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.058 |  |
| 2026-05-09 14:03:44 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.059 |  |
| 2026-05-09 14:04:26 | Katharagama (Menik Ganga) | 2.22 | 🟢 Normal | -0.080 |  |
| 2026-05-09 14:03:19 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)