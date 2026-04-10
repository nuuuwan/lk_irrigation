# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_10:19:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 10:19:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:14:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.014 |  |
| 2026-04-10 10:12:49 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.046 |  |
| 2026-04-10 10:08:22 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:08:20 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:07:37 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:07:32 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-10 10:07:29 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:06:58 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.067 |  |
| 2026-04-10 10:06:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2026-04-10 10:06:27 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:06:10 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:05:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:05:36 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:54 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:40 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.253 |  |
| 2026-04-10 10:03:36 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:28 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:18 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:09 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.041 |  |
| 2026-04-10 10:02:53 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-04-10 10:02:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.034 |  |
| 2026-04-10 10:02:07 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:51 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:43 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-10 10:01:30 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-04-10 10:01:21 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 10:01:20 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:01:04 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:00 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.022 |  |
| 2026-04-10 10:01:00 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:00:52 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.050 |  |
| 2026-04-10 10:00:43 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:00:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:00:26 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 09:58:30 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 10:01:43 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-10 10:01:21 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 10:01:00 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:00:26 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:05:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:02:07 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:05:36 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:00:43 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:08:22 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:28 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:07:29 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:18 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:54 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:06:27 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:02:53 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:19:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:01:20 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:03:36 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 10:06:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2026-04-10 10:07:32 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-10 10:06:10 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:51 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:01:04 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:00:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:07:37 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-10 10:14:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.014 |  |
| 2026-04-10 10:01:00 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.022 |  |
| 2026-04-10 10:02:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.034 |  |
| 2026-04-10 10:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-04-10 10:03:09 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.041 |  |
| 2026-04-10 10:01:30 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-04-10 10:12:49 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.046 |  |
| 2026-04-10 10:00:52 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.050 |  |
| 2026-04-10 10:06:58 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.067 |  |
| 2026-04-10 09:05:15 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.070 |  |
| 2026-04-10 10:03:40 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)