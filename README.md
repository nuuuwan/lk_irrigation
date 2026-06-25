# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_07:32:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,775 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 07:32:16 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:28:29 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:27:02 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:19:08 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:12:02 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.028 |  |
| 2026-06-25 07:10:23 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:08:17 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.018 |  |
| 2026-06-25 07:07:47 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.323 |  |
| 2026-06-25 07:07:32 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.088 |  |
| 2026-06-25 07:06:20 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:06:15 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 07:05:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:05:43 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:05:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.028 |  |
| 2026-06-25 07:05:22 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:05:09 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 07:04:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:04:19 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 07:04:14 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-06-25 07:03:56 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.045 |  |
| 2026-06-25 07:03:54 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.019 |  |
| 2026-06-25 07:03:23 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:13 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.052 |  |
| 2026-06-25 07:03:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:01 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-06-25 07:02:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-25 07:02:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.215 |  |
| 2026-06-25 07:02:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:08 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:06 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.002 |  |
| 2026-06-25 07:01:59 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:01:52 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 07:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-25 07:00:44 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:00:31 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:00:30 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 07:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-25 07:01:52 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 07:04:19 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 07:05:09 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 07:02:06 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.002 |  |
| 2026-06-25 07:02:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:23 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:28:29 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:00:44 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:01:59 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:27:02 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:32:16 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:03:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:08 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:05:43 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:19:08 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:00:31 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:05:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:10:23 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:05:22 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:02:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 07:06:15 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 07:02:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-25 07:08:17 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.018 |  |
| 2026-06-25 07:03:01 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-06-25 07:03:54 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.019 |  |
| 2026-06-25 07:04:14 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-06-25 07:12:02 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.028 |  |
| 2026-06-25 07:05:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.028 |  |
| 2026-06-25 07:03:56 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.045 |  |
| 2026-06-25 07:03:13 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.052 |  |
| 2026-06-25 07:00:30 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.080 |  |
| 2026-06-25 07:07:32 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.088 |  |
| 2026-06-25 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.215 |  |
| 2026-06-25 07:07:47 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.323 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)