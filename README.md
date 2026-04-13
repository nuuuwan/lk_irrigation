# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_04:26:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 04:26:00 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-14 04:25:46 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.269 |  |
| 2026-04-14 04:15:59 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.367 |  |
| 2026-04-14 04:13:41 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:08:57 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:07:43 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-04-14 04:06:36 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:06:10 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.367 |  |
| 2026-04-14 04:06:09 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.367 |  |
| 2026-04-14 04:06:01 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.094 |  |
| 2026-04-14 04:05:46 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:05:35 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-14 04:05:35 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:05:03 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:04:53 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-04-14 04:04:45 | Katharagama (Menik Ganga) | 0.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-14 04:04:21 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.071 |  |
| 2026-04-14 04:04:03 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.070 |  |
| 2026-04-14 04:03:55 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.024 |  |
| 2026-04-14 04:03:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:03:52 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.053 |  |
| 2026-04-14 04:03:29 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-04-14 04:03:06 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:02:57 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.029 |  |
| 2026-04-14 04:02:20 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-14 04:02:08 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 04:02:04 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-14 04:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-04-14 04:01:49 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:01:16 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.040 |  |
| 2026-04-14 04:01:13 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-14 04:00:48 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-14 04:00:26 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:00:19 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 04:00:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.118 |  |
| 2026-04-14 03:40:32 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 04:04:45 | Katharagama (Menik Ganga) | 0.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-14 04:02:04 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-14 04:00:48 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-14 04:26:00 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-14 04:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 04:02:20 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-14 04:00:19 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 03:09:33 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-14 04:05:35 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-14 04:02:08 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 04:06:36 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-14 03:04:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:03:06 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:01:49 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:05:35 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:08:57 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:05:46 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:03:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:00:26 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:13:41 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 04:07:43 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-04-14 02:02:43 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 04:01:13 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-04-14 04:03:29 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-04-14 04:04:53 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-04-14 04:03:55 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.024 |  |
| 2026-04-14 04:02:57 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.029 |  |
| 2026-04-14 04:01:16 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.040 |  |
| 2026-04-14 04:03:52 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.053 |  |
| 2026-04-14 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-04-14 04:04:03 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.070 |  |
| 2026-04-14 04:04:21 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.071 |  |
| 2026-04-14 04:06:01 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.094 |  |
| 2026-04-14 04:00:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.118 |  |
| 2026-04-14 04:25:46 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.269 |  |
| 2026-04-14 04:15:59 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.367 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)