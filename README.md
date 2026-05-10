# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_12:18:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,982 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 12:18:01 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:08:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-05-10 12:08:15 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 12:08:07 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-05-10 12:07:39 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:07:15 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:06:57 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:05:37 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-05-10 12:05:30 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:05:17 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-10 12:05:10 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-05-10 12:05:10 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-05-10 12:05:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-05-10 12:05:00 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.038 |  |
| 2026-05-10 12:04:10 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:03:48 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.086 |  |
| 2026-05-10 12:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:03:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-05-10 12:03:29 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-05-10 12:03:27 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:03:26 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.196 |  |
| 2026-05-10 12:03:08 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.051 |  |
| 2026-05-10 12:03:05 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:03:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-05-10 12:02:54 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.066 |  |
| 2026-05-10 12:02:52 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-05-10 12:02:38 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:02:36 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:02:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:02:21 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.085 |  |
| 2026-05-10 12:02:15 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:02:13 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:01:58 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.040 |  |
| 2026-05-10 12:01:37 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-05-10 12:01:36 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:01:17 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.071 |  |
| 2026-05-10 12:01:17 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:00:19 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-05-10 12:00:17 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:00:14 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 12:01:37 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-05-10 12:05:17 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-10 12:08:15 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 12:01:17 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:06:57 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:18:01 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:04:10 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:02:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:03:27 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:07:39 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:07:15 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 12:08:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-05-10 12:05:10 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-05-10 12:02:36 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:02:38 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:02:15 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-10 12:05:37 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-05-10 12:08:07 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-05-10 12:03:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-05-10 12:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:05:30 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:00:17 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:03:05 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-10 12:02:52 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-05-10 12:00:19 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-05-10 12:00:14 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-05-10 12:03:29 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-05-10 12:05:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-05-10 12:03:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-05-10 12:05:00 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.038 |  |
| 2026-05-10 12:01:58 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.040 |  |
| 2026-05-10 12:03:08 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.051 |  |
| 2026-05-10 12:05:10 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-05-10 12:02:54 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.066 |  |
| 2026-05-10 12:01:17 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.071 |  |
| 2026-05-10 12:02:21 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.085 |  |
| 2026-05-10 12:03:48 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.086 |  |
| 2026-05-10 12:03:26 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)