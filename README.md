# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_08:25:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 08:25:58 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.042 |  |
| 2026-04-14 08:25:09 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-04-14 08:15:44 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:10:39 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-04-14 08:10:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.106 |  |
| 2026-04-14 08:10:07 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:10:04 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:08:46 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.027 |  |
| 2026-04-14 08:07:15 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:06:53 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:06:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-14 08:04:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:04:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-14 08:04:03 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 08:03:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:03:18 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:03:03 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-14 08:02:54 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.059 |  |
| 2026-04-14 08:02:51 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:02:50 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:02:45 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:02:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.072 |  |
| 2026-04-14 08:02:19 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.059 |  |
| 2026-04-14 08:02:18 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-04-14 08:02:07 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-04-14 08:02:01 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:01:56 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-04-14 08:01:54 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-04-14 08:01:52 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.053 |  |
| 2026-04-14 08:01:50 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2026-04-14 08:01:45 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-04-14 08:01:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:01:25 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:01:13 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.150 |  |
| 2026-04-14 08:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-14 08:01:00 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 08:00:47 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-04-14 08:00:18 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.113 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 08:01:00 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 08:04:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-14 08:04:03 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 08:02:01 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:01:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:10:04 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:00:12 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:02:45 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:04:47 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:03:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:15:44 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:03:18 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 08:10:39 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-04-14 08:06:53 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:10:07 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:02:50 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:02:51 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:07:15 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-14 08:03:03 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-14 08:06:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-14 08:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-14 08:02:18 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-04-14 08:01:54 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-04-14 08:02:07 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-04-14 08:08:46 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.027 |  |
| 2026-04-14 08:01:45 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-04-14 08:01:56 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-04-14 08:25:09 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-04-14 07:00:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.036 |  |
| 2026-04-14 08:00:47 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-04-14 08:25:58 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.042 |  |
| 2026-04-14 08:01:50 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2026-04-14 08:01:52 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.053 |  |
| 2026-04-14 08:02:54 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.059 |  |
| 2026-04-14 08:02:19 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.059 |  |
| 2026-04-14 08:02:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.072 |  |
| 2026-04-14 08:10:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.106 |  |
| 2026-04-14 08:00:18 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.113 |  |
| 2026-04-14 08:01:13 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)