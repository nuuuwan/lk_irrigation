# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_09:12:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 09:12:27 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:11:27 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.037 |  |
| 2026-06-24 09:10:46 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.055 |  |
| 2026-06-24 09:09:11 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:08:49 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:08:33 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:07:27 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:07:25 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-24 09:06:11 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | -0.041 |  |
| 2026-06-24 09:06:06 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.031 |  |
| 2026-06-24 09:05:41 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-24 09:05:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-24 09:04:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:03:58 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:03:56 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2026-06-24 09:03:52 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-06-24 09:03:23 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.060 |  |
| 2026-06-24 09:03:15 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:03:13 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:03:00 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.070 |  |
| 2026-06-24 09:02:44 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.128 |  |
| 2026-06-24 09:02:27 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-06-24 09:02:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-06-24 09:02:21 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 09:02:05 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:01:57 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:01:45 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:01:40 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:01:39 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:01:34 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.040 |  |
| 2026-06-24 09:01:26 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | -0.031 |  |
| 2026-06-24 09:01:09 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-24 09:00:32 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.050 |  |
| 2026-06-24 09:00:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-24 09:00:16 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:00:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 08:33:21 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.070 |  |
| 2026-06-24 09:01:09 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-06-24 09:05:41 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-24 09:05:32 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-24 09:02:21 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 09:07:25 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-24 09:00:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:01:57 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:01:39 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:08:49 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 09:03:00 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-24 08:02:09 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:00:16 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:03:15 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:04:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:01:40 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:07:27 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:12:27 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-24 09:09:11 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:03:58 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:02:05 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:01:45 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:08:33 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:03:13 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-06-24 09:00:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-24 09:03:56 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2026-06-24 09:02:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-06-24 09:02:27 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-06-24 09:03:52 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-06-24 09:06:06 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.031 |  |
| 2026-06-24 09:01:26 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | -0.031 |  |
| 2026-06-24 09:11:27 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.037 |  |
| 2026-06-24 09:01:34 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.040 |  |
| 2026-06-24 09:06:11 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | -0.041 |  |
| 2026-06-24 09:00:32 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.050 |  |
| 2026-06-24 09:10:46 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.055 |  |
| 2026-06-24 09:03:23 | Hanwella (Kelani Ganga) | 2.89 | 🟢 Normal | -0.060 |  |
| 2026-06-24 09:02:44 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)