# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_13:00:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 13:00:44 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 13:00:25 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2026-06-11 12:15:24 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-11 12:12:48 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 12:10:24 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 12:15:24 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-11 12:00:27 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-11 12:06:40 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-11 12:00:59 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-11 12:00:42 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-11 12:02:12 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 12:12:48 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 12:06:43 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 12:10:24 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 12:03:17 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 12:03:45 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 12:05:16 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 12:05:39 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 12:06:54 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 12:00:25 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:01:17 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:07:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:05:59 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:02:51 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:03:57 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:06:56 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:04:27 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:01:41 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:02:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 13:00:44 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:03:14 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:01:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:02:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 12:04:43 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-06-11 12:02:54 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-06-11 12:04:29 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-06-11 12:03:09 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-11 12:00:09 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-11 12:00:13 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.011 |  |
| 2026-06-11 12:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-11 12:00:55 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2026-06-11 13:00:25 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2026-06-11 12:06:15 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)