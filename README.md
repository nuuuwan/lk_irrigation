# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_08:18:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 08:18:15 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:17:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | -0.033 |  |
| 2026-06-27 08:15:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:14:11 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-06-27 08:14:05 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:12:11 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:10:54 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.027 |  |
| 2026-06-27 08:10:19 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:08:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:08:02 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-27 08:06:14 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 08:05:55 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:05:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:56 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:53 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.081 |  |
| 2026-06-27 08:04:49 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-27 08:04:34 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:31 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.023 |  |
| 2026-06-27 08:04:30 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:25 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 08:04:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:24 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-06-27 08:04:20 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 08:04:19 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:14 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -90.000 |  |
| 2026-06-27 08:04:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 08:04:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -90.000 |  |
| 2026-06-27 08:03:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:03:27 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-27 08:02:47 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:02:25 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.099 |  |
| 2026-06-27 08:02:15 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 08:02:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:02:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:02:07 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.033 |  |
| 2026-06-27 08:01:58 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:54 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:51 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:28 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -90.000 |  |
| 2026-06-27 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:09 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-27 08:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-06-27 07:59:53 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 08:04:25 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 08:04:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 08:02:15 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 08:06:14 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 08:04:20 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 08:10:19 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:02:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:30 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:05:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:02:47 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:54 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:56 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:05:55 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:12:11 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:08:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:02:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:19 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:15:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:58 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:18:15 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:03:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:01:51 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 08:04:49 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-27 08:01:09 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-27 08:03:27 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:59:53 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.013 |  |
| 2026-06-27 08:04:24 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-06-27 08:08:02 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-27 08:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-06-27 08:04:31 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.023 |  |
| 2026-06-27 08:10:54 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.027 |  |
| 2026-06-27 08:14:11 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-06-27 08:17:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | -0.033 |  |
| 2026-06-27 08:02:07 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.033 |  |
| 2026-06-27 08:04:53 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.081 |  |
| 2026-06-27 08:02:25 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.099 |  |
| 2026-06-27 08:04:14 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)