# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_21:19:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 21:19:55 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:11:04 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.081 |  |
| 2026-06-21 21:08:09 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:06:53 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-21 21:06:33 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-06-21 21:05:51 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-06-21 21:05:27 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:04:58 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 21:04:55 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:04:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 21:04:34 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-21 21:04:09 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.049 |  |
| 2026-06-21 21:04:00 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:24 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:22 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:13 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:08 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:56 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 21:02:43 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:36 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-06-21 21:02:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.132 |  |
| 2026-06-21 21:02:32 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:31 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:20 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.472 | 🔺 Rising |
| 2026-06-21 21:02:18 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:16 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-21 21:02:03 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:01:48 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:41 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:22 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-21 21:01:15 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:00:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:00:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 21:02:20 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.472 | 🔺 Rising |
| 2026-06-21 21:06:33 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-06-21 21:01:22 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-21 21:06:53 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-21 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-21 21:04:34 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-21 21:04:58 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 21:02:56 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 21:02:03 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 21:04:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 21:02:32 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:00:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:15 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:19:55 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:24 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:08:09 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:13 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:04:00 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:18 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:43 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:04:55 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:08 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:22 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:05:27 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:02:31 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:48 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:41 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:00:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:02:16 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 21:02:36 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-06-21 21:05:51 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-06-21 21:04:09 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.049 |  |
| 2026-06-21 21:11:04 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.081 |  |
| 2026-06-21 21:02:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)