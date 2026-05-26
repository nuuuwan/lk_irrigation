# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_13:12:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,167 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 13:12:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:10:43 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:09:53 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 13:09:29 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 13:09:25 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:08:07 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-05-26 13:07:46 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-26 13:07:23 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:07:13 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-26 13:07:03 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-26 13:06:37 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 13:06:25 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.135 |  |
| 2026-05-26 13:06:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:06:15 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:05:56 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | -0.095 |  |
| 2026-05-26 13:05:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 13:04:58 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:04:27 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.029 |  |
| 2026-05-26 13:03:40 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 13:03:33 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:03:32 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-26 13:03:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 13:03:23 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-26 13:03:20 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:02:59 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:02:42 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | -0.063 |  |
| 2026-05-26 13:02:29 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:02:21 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-05-26 13:02:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.015 |  |
| 2026-05-26 13:01:57 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:01:39 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-05-26 13:01:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-05-26 13:01:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:00:51 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:00:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:00:32 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 12:58:02 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 13:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-26 13:07:46 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-26 13:03:32 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-26 13:03:23 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-26 13:09:53 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 13:07:13 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-26 13:06:37 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 13:09:29 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 13:05:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 13:03:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 13:03:40 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 12:58:02 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:03:20 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:00:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:00:32 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:04:58 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:07:23 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:06:15 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:06:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:02:59 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:10:43 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:12:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:07:03 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:00:51 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:09:25 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:01:57 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:03:33 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 13:08:07 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-05-26 13:04:27 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:02:29 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:01:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-26 13:01:39 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-05-26 13:01:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-05-26 13:02:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.015 |  |
| 2026-05-26 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.029 |  |
| 2026-05-26 13:02:21 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-05-26 13:02:42 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | -0.063 |  |
| 2026-05-26 13:05:56 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | -0.095 |  |
| 2026-05-26 13:06:25 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)