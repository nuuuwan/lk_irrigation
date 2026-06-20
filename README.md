# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_23:12:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,881 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 23:12:46 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-20 23:10:04 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-06-20 23:09:55 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:07:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-06-20 23:06:02 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-06-20 23:05:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:05:15 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:05:14 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-20 23:04:50 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:04:41 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:04:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-20 23:04:16 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:04:03 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:53 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 23:03:39 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:03:27 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:03:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:21 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:03:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:15 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-20 23:03:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:02 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:02:56 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.025 |  |
| 2026-06-20 23:02:51 | Dunamale (Aththanagalu Oya) | 1.51 | 🟢 Normal | -0.014 |  |
| 2026-06-20 23:02:40 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:02:21 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.099 |  |
| 2026-06-20 23:01:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:25 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:16 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:00:35 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:25:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 23:03:15 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-20 23:03:53 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 23:02:40 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:04:03 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:00:35 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:05:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:09:55 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:19 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:04:16 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:04:50 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:16 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:06:05 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:03:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 23:01:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 22:25:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.007 |  |
| 2026-06-20 22:24:11 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.008 |  |
| 2026-06-20 23:10:04 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.009 |  |
| 2026-06-20 23:12:46 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-06-20 23:04:41 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-20 22:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:03:21 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:01:25 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:03:27 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-20 23:03:39 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 23:05:14 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-06-20 23:02:51 | Dunamale (Aththanagalu Oya) | 1.51 | 🟢 Normal | -0.014 |  |
| 2026-06-20 23:04:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-20 22:01:12 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-06-20 23:02:56 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.025 |  |
| 2026-06-20 23:06:02 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-06-20 23:07:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-06-20 23:02:21 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)