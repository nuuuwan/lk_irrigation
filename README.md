# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_09:14:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 09:14:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:08:20 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:07:40 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.038 |  |
| 2026-06-03 09:07:20 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 09:07:12 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2026-06-03 09:06:57 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:05:40 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:05:28 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.033 |  |
| 2026-06-03 09:05:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:05:09 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-06-03 09:04:55 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:04:54 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:53 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:49 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:34 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-03 09:04:13 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:04:10 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:04:03 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:52 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:48 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:45 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 09:03:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-06-03 09:03:24 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:19 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:13 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:02:59 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.030 |  |
| 2026-06-03 09:02:59 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:42 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-06-03 09:02:40 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-03 09:02:04 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-06-03 09:02:01 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 09:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 09:01:37 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.038 |  |
| 2026-06-03 09:01:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.050 |  |
| 2026-06-03 09:00:30 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:00:23 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 09:02:40 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-03 09:02:01 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 09:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 09:07:20 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 09:03:45 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 09:03:48 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:52 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:01:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:19 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:54 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:08:20 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:03 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:13 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:14:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:49 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:04:53 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:59 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:05:13 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:00:30 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:03:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:00:23 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:06:57 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-03 09:07:12 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.009 |  |
| 2026-06-03 09:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:04:55 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:04:10 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:04:13 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-03 09:03:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-06-03 09:04:34 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-03 09:02:42 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-06-03 09:05:09 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-06-03 09:02:59 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.030 |  |
| 2026-06-03 09:05:28 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.033 |  |
| 2026-06-03 09:01:37 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.038 |  |
| 2026-06-03 09:07:40 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.038 |  |
| 2026-06-03 09:02:04 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-06-03 09:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)