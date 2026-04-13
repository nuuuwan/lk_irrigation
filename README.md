# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_09:12:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 09:12:02 | Galgamuwa (Mee Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-13 09:10:14 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.029 |  |
| 2026-04-13 09:09:14 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.103 |  |
| 2026-04-13 09:07:54 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:07:36 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.076 |  |
| 2026-04-13 09:07:24 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:07:12 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-13 09:06:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:06:48 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 09:06:36 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-13 09:06:31 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 09:06:14 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:06:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 09:05:59 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-13 09:05:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:05:25 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-13 09:05:15 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-04-13 09:05:13 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 09:04:56 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 09:04:48 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-04-13 09:04:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:04:19 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.127 |  |
| 2026-04-13 09:04:08 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-13 09:03:48 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-13 09:03:41 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-04-13 09:03:25 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:03:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:03:09 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 09:02:46 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-13 09:02:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 09:02:25 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:02:20 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-13 09:02:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:01:36 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:01:29 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-04-13 09:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 09:01:11 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.071 |  |
| 2026-04-13 09:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 09:05:59 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-13 09:03:48 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-13 09:07:12 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-13 09:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 09:03:09 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 09:06:31 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 09:05:13 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 09:06:48 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 09:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 09:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 09:06:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 09:04:56 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 09:03:25 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:06:14 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:02:25 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:07:24 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:05:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:02:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:04:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:03:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:02:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:07:54 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:01:36 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 09:05:25 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-13 09:12:02 | Galgamuwa (Mee Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-13 09:06:36 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-13 09:05:15 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-04-13 09:02:46 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-04-13 09:02:20 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-13 09:04:08 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-04-13 09:03:41 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-04-13 09:01:29 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-04-13 09:04:48 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-04-13 09:10:14 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.029 |  |
| 2026-04-13 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.071 |  |
| 2026-04-13 09:07:36 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.076 |  |
| 2026-04-13 09:09:14 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.103 |  |
| 2026-04-13 09:04:19 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)