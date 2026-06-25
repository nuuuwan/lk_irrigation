# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_06:19:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,734 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 06:19:06 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:14:13 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:13:22 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-06-25 06:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | -45.000 |  |
| 2026-06-25 06:12:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -45.000 |  |
| 2026-06-25 06:11:44 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:10:22 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:07:09 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-25 06:06:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:06:41 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-25 06:06:36 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.024 |  |
| 2026-06-25 06:06:28 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.036 |  |
| 2026-06-25 06:06:25 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-06-25 06:05:59 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:05:53 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-25 06:05:08 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.067 |  |
| 2026-06-25 06:04:36 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:04:34 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.002 |  |
| 2026-06-25 06:03:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:03:00 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:02:59 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.022 |  |
| 2026-06-25 06:02:45 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-25 06:02:43 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-06-25 06:02:37 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 06:02:28 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.011 |  |
| 2026-06-25 06:02:26 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-25 06:02:26 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-25 06:02:23 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:02:22 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:02:17 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 06:02:16 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:01:56 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-25 06:01:48 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 06:01:42 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-25 06:01:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:01:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-25 06:01:24 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 06:01:00 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:00:14 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 05:57:38 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -3.493 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 06:05:53 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-25 06:01:56 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-25 06:01:48 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 06:01:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-25 06:00:14 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 06:07:09 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-25 06:02:17 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 06:02:37 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 06:01:24 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 06:02:22 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:14:13 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:06:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:05:59 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:03:00 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:10:22 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:03:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:01:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:02:23 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:04:36 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:19:06 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:02:16 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 06:04:34 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.002 |  |
| 2026-06-25 06:06:25 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-06-25 06:02:26 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-25 06:02:26 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-25 06:06:41 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-25 06:01:42 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-25 06:02:28 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.011 |  |
| 2026-06-25 06:13:22 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-06-25 06:02:45 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-25 06:02:59 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.022 |  |
| 2026-06-25 06:06:36 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.024 |  |
| 2026-06-25 06:06:28 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.036 |  |
| 2026-06-25 06:02:43 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-06-25 06:05:08 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.067 |  |
| 2026-06-25 05:57:38 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -3.493 |  |
| 2026-06-25 06:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | -45.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)