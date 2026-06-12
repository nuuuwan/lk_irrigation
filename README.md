# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_09:13:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 09:13:48 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:08:23 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:07:34 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | -0.131 |  |
| 2026-06-12 09:07:30 | Magura (Kalu Ganga) | 4.74 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-06-12 09:07:02 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:06:56 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-12 09:06:50 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 09:06:49 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-12 09:06:24 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-12 09:06:23 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-12 09:06:20 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.037 |  |
| 2026-06-12 09:06:04 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-06-12 09:05:51 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 09:05:44 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-12 09:05:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 09:05:07 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 09:04:33 | Rathnapura (Kalu Ganga) | 5.91 | 🟡 Alert | -0.071 |  |
| 2026-06-12 09:04:07 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 09:03:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:03:55 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:03:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 09:03:08 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-12 09:02:59 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.030 |  |
| 2026-06-12 09:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-12 09:02:45 | Thawalama (Gin Ganga) | 3.70 | 🟢 Normal | -0.053 |  |
| 2026-06-12 09:02:24 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:02:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:02:21 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 09:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-06-12 09:02:15 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.111 |  |
| 2026-06-12 09:01:54 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-06-12 09:01:53 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-12 09:01:47 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:01:40 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:01:26 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.062 |  |
| 2026-06-12 09:01:09 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-12 09:00:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:00:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-06-12 09:00:09 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 09:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-06-12 09:07:30 | Magura (Kalu Ganga) | 4.74 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-06-12 09:04:33 | Rathnapura (Kalu Ganga) | 5.91 | 🟡 Alert | -0.071 |  |
| 2026-06-12 09:01:54 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-06-12 09:01:09 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-12 09:06:24 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-12 09:06:23 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-12 09:03:08 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-12 09:05:51 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 09:05:07 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 09:06:49 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-12 09:04:07 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 09:05:44 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-12 09:06:56 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-12 09:02:21 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 09:06:50 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 09:03:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 09:05:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 09:08:23 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:00:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:02:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:00:09 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:01:40 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:07:02 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:01:47 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:03:55 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:03:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:02:24 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:13:48 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-12 09:06:04 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-06-12 09:00:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-06-12 09:01:53 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-12 09:02:59 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.030 |  |
| 2026-06-12 09:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-12 09:06:20 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.037 |  |
| 2026-06-12 09:02:45 | Thawalama (Gin Ganga) | 3.70 | 🟢 Normal | -0.053 |  |
| 2026-06-12 09:01:26 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.062 |  |
| 2026-06-12 09:02:15 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.111 |  |
| 2026-06-12 09:07:34 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)