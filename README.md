# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_15:08:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,589 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 15:08:39 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:08:33 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-06-20 15:07:40 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-20 15:07:28 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-06-20 15:07:26 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-06-20 15:07:19 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.092 |  |
| 2026-06-20 15:06:04 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-06-20 15:05:33 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.009 |  |
| 2026-06-20 15:04:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:04:36 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:41 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:23 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:13 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:03:13 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:06 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 15:03:03 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-06-20 15:02:58 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:02:54 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:53 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:50 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 15:02:43 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:24 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.062 |  |
| 2026-06-20 15:02:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:02:16 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.055 |  |
| 2026-06-20 15:02:16 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-06-20 15:02:14 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:02:11 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 15:02:11 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.012 |  |
| 2026-06-20 15:02:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:06 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:01 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 15:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:01:51 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 15:01:19 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:01:07 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:00:37 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 15:07:40 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-20 15:02:01 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-20 15:02:11 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 15:01:51 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 15:03:06 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 15:02:50 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 15:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:43 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:53 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:04:36 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:23 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:24 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:08:39 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:54 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:01:07 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:41 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:03:13 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:04:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:02:06 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 15:08:33 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-06-20 15:05:33 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.009 |  |
| 2026-06-20 15:02:17 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:02:58 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:01:19 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:02:14 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:03:13 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-20 15:02:11 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.012 |  |
| 2026-06-20 15:06:04 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-06-20 15:07:26 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-06-20 15:02:16 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-06-20 15:03:03 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-06-20 15:00:37 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.031 |  |
| 2026-06-20 15:07:28 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-06-20 15:02:16 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.055 |  |
| 2026-06-20 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.062 |  |
| 2026-06-20 15:07:19 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)