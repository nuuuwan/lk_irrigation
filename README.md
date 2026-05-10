# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_16:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 16:18:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.008 |  |
| 2026-05-10 16:18:20 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.008 |  |
| 2026-05-10 16:17:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-05-10 16:17:00 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:16:20 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.008 |  |
| 2026-05-10 16:11:09 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-05-10 16:09:56 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:09:34 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:09:08 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:09:06 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:07:12 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -0.077 |  |
| 2026-05-10 16:06:59 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.028 |  |
| 2026-05-10 16:06:46 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:06:04 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-05-10 16:05:00 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-10 16:04:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:04:14 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-10 16:04:11 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-05-10 16:04:01 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:03:41 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:03:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-10 16:03:40 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-05-10 16:03:37 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-05-10 16:03:34 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:03:23 | Katharagama (Menik Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:03:22 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.086 |  |
| 2026-05-10 16:03:03 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-10 16:02:58 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:56 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 16:02:36 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:33 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:02:22 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.040 |  |
| 2026-05-10 16:02:12 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:08 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:01:53 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-05-10 16:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:01:38 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-10 16:01:29 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.045 |  |
| 2026-05-10 16:01:04 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-05-10 16:00:45 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 16:03:03 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-10 16:05:00 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-10 16:03:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-10 16:02:56 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 16:04:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:36 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:09:56 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:17:00 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:03:34 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:58 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:09:34 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:02:08 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:00:45 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:03:41 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:06:46 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-10 16:18:20 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.008 |  |
| 2026-05-10 16:16:20 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.008 |  |
| 2026-05-10 16:18:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.008 |  |
| 2026-05-10 16:17:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-05-10 16:04:01 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:02:33 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:09:08 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:03:23 | Katharagama (Menik Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-10 16:01:38 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-10 16:04:11 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-05-10 16:01:04 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-05-10 16:11:09 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-05-10 16:04:14 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-10 16:06:04 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-05-10 16:03:40 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-05-10 16:06:59 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.028 |  |
| 2026-05-10 16:01:53 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-05-10 16:03:37 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-05-10 16:02:22 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.040 |  |
| 2026-05-10 16:01:29 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.045 |  |
| 2026-05-10 16:07:12 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -0.077 |  |
| 2026-05-10 16:03:22 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)