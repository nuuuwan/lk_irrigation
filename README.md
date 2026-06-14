# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_20:16:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 20:16:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:15:53 | Panadugama (Nilwala Ganga) | 0.95 | 🟢 Normal | -11.713 |  |
| 2026-06-14 20:15:50 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:11:44 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.017 |  |
| 2026-06-14 20:10:31 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-06-14 20:09:03 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:08:36 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.027 |  |
| 2026-06-14 20:08:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.041 |  |
| 2026-06-14 20:07:32 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -11.713 |  |
| 2026-06-14 20:07:08 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:06:55 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:06:41 | Rathnapura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.058 |  |
| 2026-06-14 20:05:55 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.019 |  |
| 2026-06-14 20:05:43 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-14 20:05:38 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-06-14 20:05:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-14 20:05:00 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:04:58 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.029 |  |
| 2026-06-14 20:04:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-06-14 20:04:07 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.107 |  |
| 2026-06-14 20:03:39 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:03:36 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:03:20 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-14 20:03:01 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:02:54 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:02:38 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -0.089 |  |
| 2026-06-14 20:02:37 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.060 |  |
| 2026-06-14 20:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:02:07 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:01:51 | Dunamale (Aththanagalu Oya) | 2.85 | 🟢 Normal | -0.030 |  |
| 2026-06-14 20:01:45 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:01:43 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:01:05 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.045 |  |
| 2026-06-14 20:00:25 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:00:10 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 20:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.041 |  |
| 2026-06-14 20:05:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-14 20:03:20 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-14 20:00:10 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:09:03 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:01:45 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:08:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:01:43 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:06:55 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:00:25 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:03:01 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:03:36 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:03:39 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:05:00 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:16:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 20:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-14 19:21:15 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-14 20:15:50 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:07:08 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:02:07 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-14 20:11:44 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.017 |  |
| 2026-06-14 20:05:55 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.019 |  |
| 2026-06-14 20:05:43 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-14 20:08:36 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.027 |  |
| 2026-06-14 20:10:31 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-06-14 20:04:58 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.029 |  |
| 2026-06-14 20:01:51 | Dunamale (Aththanagalu Oya) | 2.85 | 🟢 Normal | -0.030 |  |
| 2026-06-14 20:05:38 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-06-14 20:01:05 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.045 |  |
| 2026-06-14 20:06:41 | Rathnapura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.058 |  |
| 2026-06-14 20:02:37 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.060 |  |
| 2026-06-14 20:04:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-06-14 20:02:38 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -0.089 |  |
| 2026-06-14 20:04:07 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.107 |  |
| 2026-06-14 20:15:53 | Panadugama (Nilwala Ganga) | 0.95 | 🟢 Normal | -11.713 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)