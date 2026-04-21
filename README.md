# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_10:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,971 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 10:18:13 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:16:45 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:10:43 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.073 |  |
| 2026-04-21 10:10:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-04-21 10:09:47 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-04-21 10:08:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:07:52 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.155 |  |
| 2026-04-21 10:07:35 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 10:06:42 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-21 10:06:26 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-04-21 10:05:53 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:05:40 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-04-21 10:05:10 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-04-21 10:04:45 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-04-21 10:04:33 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 10:04:17 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:04:05 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.066 |  |
| 2026-04-21 10:03:56 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 10:03:37 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-21 10:03:35 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.190 |  |
| 2026-04-21 10:03:19 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:03:08 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-04-21 10:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-21 10:02:40 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:02:34 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2026-04-21 10:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.049 |  |
| 2026-04-21 10:02:25 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-04-21 10:02:17 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 10:02:14 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.090 |  |
| 2026-04-21 10:02:12 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.082 |  |
| 2026-04-21 10:02:05 | Kithulgala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.088 |  |
| 2026-04-21 10:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-04-21 10:00:56 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:00:49 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.044 |  |
| 2026-04-21 10:00:48 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.047 |  |
| 2026-04-21 10:00:34 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:00:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-21 10:00:23 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:00:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 09:58:39 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 10:05:10 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-04-21 09:03:26 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 10:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-21 10:04:33 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 10:07:35 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 10:06:42 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-21 10:02:17 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 10:03:56 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 10:00:23 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:18:13 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:00:34 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:04:17 | Galgamuwa (Mee Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:02:40 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:03:19 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:00:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:05:53 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:08:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:16:45 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-21 10:06:26 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-04-21 10:02:25 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-04-21 10:09:47 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-04-21 10:10:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-04-21 10:00:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-04-21 10:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-04-21 10:05:40 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-04-21 10:03:37 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-21 10:04:45 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-04-21 10:03:08 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-04-21 10:00:49 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.044 |  |
| 2026-04-21 10:00:48 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.047 |  |
| 2026-04-21 10:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.049 |  |
| 2026-04-21 10:02:34 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2026-04-21 10:04:05 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.066 |  |
| 2026-04-21 10:10:43 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.073 |  |
| 2026-04-21 10:02:12 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.082 |  |
| 2026-04-21 10:02:05 | Kithulgala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.088 |  |
| 2026-04-21 10:02:14 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.090 |  |
| 2026-04-21 10:07:52 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.155 |  |
| 2026-04-21 10:03:35 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)