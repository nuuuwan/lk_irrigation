# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_00:14:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 00:14:20 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-06-21 00:13:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-21 00:12:25 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.022 |  |
| 2026-06-21 00:12:16 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:07:23 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-06-21 00:06:02 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-06-21 00:05:17 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-21 00:05:05 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:04:59 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:04:24 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:04:06 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:03:59 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:03:41 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:03:33 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-21 00:02:55 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:31 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:29 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:26 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-21 00:02:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:21 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:14 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-21 00:02:05 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:04 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:01 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:47 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:36 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:21 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:00:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 00:00:14 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 23:03:15 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-21 00:13:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-21 00:05:17 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-21 00:03:33 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-21 00:00:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 00:00:14 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:04:24 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:55 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:36 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:03:59 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:04 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:12:16 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:04:59 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:03:41 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:05:05 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:01:47 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:04:06 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-21 00:02:05 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:25:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.007 |  |
| 2026-06-20 23:10:04 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-06-21 00:02:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:01:21 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:29 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:31 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:01 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-21 00:02:21 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-21 00:14:20 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-06-21 00:07:23 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-06-21 00:02:14 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-21 00:02:26 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-06-21 00:12:25 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.022 |  |
| 2026-06-21 00:06:02 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-06-20 23:07:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)