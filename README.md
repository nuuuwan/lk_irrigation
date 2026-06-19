# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_02:39:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,086 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 02:39:05 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-06-20 02:19:38 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:18:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -1.070 |  |
| 2026-06-20 02:18:14 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -1.070 |  |
| 2026-06-20 02:11:25 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -4.500 |  |
| 2026-06-20 02:11:09 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -4.500 |  |
| 2026-06-20 02:09:26 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:06:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-20 02:06:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-06-20 02:06:01 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:05:24 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-06-20 02:05:13 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-20 02:05:09 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:05:02 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-06-20 02:03:48 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:03:44 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.023 |  |
| 2026-06-20 02:03:25 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -1.070 |  |
| 2026-06-20 02:03:18 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:03:18 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-06-20 02:02:47 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:02:35 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-06-20 02:02:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:02:10 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-20 02:02:00 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-20 02:02:00 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -4.500 |  |
| 2026-06-20 02:01:44 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -4.500 |  |
| 2026-06-20 02:01:42 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:40 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 22:06:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-20 02:05:24 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-06-20 02:06:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-20 02:02:10 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:08 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:06 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:00:52 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:42 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 01:03:57 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:06:01 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:09:26 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-06-20 01:01:12 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:02:47 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:40 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:19:38 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:03:48 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:05:09 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:03:18 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:02:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 01:08:17 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-06-20 02:05:02 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-06-20 02:02:35 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-06-20 02:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 02:03:18 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-06-20 01:00:37 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.013 |  |
| 2026-06-20 02:05:13 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-20 02:06:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-06-20 02:02:00 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-20 02:39:05 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-06-20 02:03:44 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.023 |  |
| 2026-06-19 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.033 |  |
| 2026-06-20 02:18:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -1.070 |  |
| 2026-06-20 02:02:00 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -4.500 |  |
| 2026-06-20 02:11:25 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)