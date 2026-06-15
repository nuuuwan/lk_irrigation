# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_09:25:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 09:25:13 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:13:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:08:46 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:08:10 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:07:23 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.028 |  |
| 2026-06-15 09:07:17 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-06-15 09:06:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-15 09:06:28 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.141 |  |
| 2026-06-15 09:06:11 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-06-15 09:05:56 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:05:39 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:05:37 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-06-15 09:05:13 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.057 |  |
| 2026-06-15 09:05:09 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:05:03 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:04:41 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-15 09:04:27 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.029 |  |
| 2026-06-15 09:04:15 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:04:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:03:52 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 09:03:47 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.082 |  |
| 2026-06-15 09:03:43 | Ellagawa (Kalu Ganga) | 6.53 | 🟢 Normal | -0.090 |  |
| 2026-06-15 09:03:09 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.030 |  |
| 2026-06-15 09:03:04 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:03:03 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:02:36 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:02:27 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:02:22 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:02:21 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.080 |  |
| 2026-06-15 09:01:53 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:01:39 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-06-15 09:01:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:00:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 09:00:51 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-06-15 09:00:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:00:18 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-06-15 09:00:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 09:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.080 |  |
| 2026-06-15 09:05:37 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-06-15 09:06:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-15 09:03:52 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 09:04:41 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-15 09:00:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 09:02:21 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:00:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:01:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:02:27 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:00:51 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:04:15 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:59:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:13:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:03:03 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:04:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:08:10 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:02:22 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:25:13 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:05:03 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:05:56 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:08:46 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:00:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-15 09:07:17 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-06-15 09:05:39 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:05:09 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:02:36 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:01:53 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-15 09:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-06-15 09:07:23 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.028 |  |
| 2026-06-15 09:04:27 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.029 |  |
| 2026-06-15 09:01:39 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-06-15 09:03:09 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.030 |  |
| 2026-06-15 09:06:11 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-06-15 09:00:18 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-06-15 09:05:13 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.057 |  |
| 2026-06-15 09:03:47 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.082 |  |
| 2026-06-15 09:03:43 | Ellagawa (Kalu Ganga) | 6.53 | 🟢 Normal | -0.090 |  |
| 2026-06-15 09:06:28 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)